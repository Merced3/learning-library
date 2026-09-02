# Crash-Proofing: What One Learner Discovered Building a Discord Bot

An interview-format review of deep-dive nodes 1–3, with built-in prediction pauses.

---

**HOST:** Welcome back. Today we're doing something a little different. A few days ago, Merced — not a professional engineer, someone learning software by building his own projects with AI — went through a sequence of lessons about a Discord bot he built called Socratic Partner. What he learned surprised him, and how he learned it might surprise you. Merced, welcome.

**MERCED:** Thanks for having me. And I should be honest up front: my track record with this stuff isn't great. A few days before these lessons, I was quizzed on five concepts I'd heard explained to me — and I retained zero of them. Zero out of five.

**HOST:** Zero. And yet today you can walk through some genuinely subtle distributed-systems ideas. So what changed?

**MERCED:** The difference between hearing an answer and being forced to produce one. That's the whole story, really.

**HOST:** Let's get concrete. Your bot has a flow where the user types "done," and the bot summarizes the conversation, posts the summary to Discord, and marks the conversation complete in a database. Simple enough. Now — the first thing your teacher asked you was deceptively simple. I'm going to ask you, and I want listeners to answer it too, because there's a pause coming. Here it is.

The process crashes. Somewhere in that flow, the program just dies. Where exactly does the crash do damage?

If you're listening, try to actually answer before the pause ends. Not "the program could crash" — where, between which steps, does the crash hurt?

... ... ...

**MERCED:** And when I was asked this, I gave the answer everyone gives: "before the database write." It sounds right. It's wrong.

**HOST:** Why is it wrong?

**MERCED:** Because the interesting boundary isn't the database. Walk the flow slowly. Step one: mark the conversation CLOSING in the database — a durable write, it survives a crash. Step two: call the language model to write the summary — that costs money and returns text, but nothing is durable yet. Step three: send the summary to Discord — and here's the thing about sending a message: once Discord's servers accept it, the message exists in the world. It's visible. That's not something your program controls anymore. Step four: write COMPLETED in the database.

The crash window — the dangerous gap — is between step three and step four.

**HOST:** Between "Discord has the message" and "the database knows about it."

**MERCED:** Exactly. If the process dies in that gap, then on restart the database says the conversation is still closing. The summary is out there in Discord, but your system has no record of it. And now every recovery option is bad: re-send the message and you've posted a duplicate — spam. Don't re-send it and the summary is orphaned — loss. You can't tell which world you're in, because the one thing that would tell you — the database record — is precisely what didn't happen.

**HOST:** And that's the definition you landed on. A crash window is...

**MERCED:** A span between two durable steps where a crash leaves the system's record out of sync with reality. And the game of reliable design is shrinking that window — pushing it toward one operation you can't crash in the middle of.

**HOST:** Hold that phrase — "one operation you can't crash in the middle of" — because it becomes the next lesson. But first: your bot actually solves this. How?

**MERCED:** By making the in-between state visible. CLOSING isn't just a label, it's a promise: "a crash here is expected, and recoverable." On restart, the system sees CLOSING and knows: something was in flight. Reopen the conversation, let the user retry "done" cleanly. The state machine — OPEN, CLOSING, COMPLETED — exists so that no crash can leave the system in a state it can't describe.

**HOST:** Okay, second concept, and this is the one you told me frustrated you the most. The scenario: two things must be written to the database — say, a charge record and an updated balance — and a crash could happen between them. Your first guess at what a transaction does was, quote, "it makes the crash window smaller." Why is that wrong?

**MERCED:** Because it doesn't make the window smaller. It makes the window *harmless*. The window is still there — the program can still die mid-sequence. But a transaction welds the two writes into one indivisible unit. Either both writes land, or neither does. There is no world where the database contains the charge but not the balance update. If the crash happens mid-transaction, the database rolls back — discards everything — and both writes vanish together.

**HOST:** So the guarantee isn't "crashes become rare"—

**MERCED:** It's "crashes can't split the pair." The invariant — the thing that must always be true, "charges and balances move together" — survives the crash, because the crash can only ever see the before-state or the after-state. Never the middle.

**HOST:** Prediction pause for listeners, because this one has a trap. After a crash in the middle of a transaction, what does the database show? (a) The first write but not the second. (b) Both writes. (c) Neither write.

... ... ...

**MERCED:** And I'll admit — I answered correctly, "neither," but I flagged it myself as a protective guess. "The safe answer is probably the one where nothing bad happened." Knowing the right answer and knowing *why* it's right turned out to be different things. The why is the mechanism: the database doesn't publish any of the transaction's writes until all of them succeed. Mid-crash, nothing was ever published. "Neither" isn't the lucky outcome — it's the only possible outcome.

**HOST:** Now here's where it got hard for you, because there's a limit to this magic, and it took a while to click. The full flow is: mark CLOSING, call the model, send the Discord message, write COMPLETED. Which of those steps can live inside a transaction?

**MERCED:** Only the database writes. And that was my big mistake — I wanted to put the model call and the Discord send inside the transaction too. Wrap everything in one big safe envelope.

**HOST:** Why can't you?

**MERCED:** Because rollback only reaches the database. If the transaction rolls back, the database can un-write a row. It cannot un-spend the money you paid the model. It cannot un-send a message that Discord already delivered. Outside-world actions can never live inside a transaction — there is no undo for reality.

**HOST:** So the envelope rule is—

**MERCED:** Each database step is its own envelope. Durable things group together; world-facing actions stay outside, and you handle their crashes with recovery logic, not rollback. And one more thing that sounds like a joke but isn't: a single write needs no transaction wrapper at all. One row, all-or-nothing — that's automatic.

**HOST:** Third concept. A race. And this is where your teacher found your pattern — you'd been answering questions "one layer up," giving true answers at the wrong level of the system. The scenario: to close a conversation, the naive code first *checks* — "is this conversation open?" — and then *acts* — "update it to CLOSING." Two separate database operations. Two requests arrive at the same time. What breaks?

Listeners, the trap is to answer "well, under heavy load, thousands of requests..." Resist it. How many requests does it take to break this?

... ... ...

**MERCED:** Two. That's what got me. No load, no stress, no thousands of users. Just two. Because the check and the act are two *moments*, and time passes between them. Request A checks — open. Request B checks — open. Both saw a world where closing was allowed. A acts. B acts. Both believe they closed the conversation. Duplicate completion work runs.

**HOST:** And the fix?

**MERCED:** Collapse check-and-act into one guarded write. In plain words: "set this to CLOSING **if** it's currently OPEN" — as a single operation. The database runs row writes one at a time; it's a single writer per row. So A's guarded write lands first. B's arrives, checks its "if," and the if is false now — B writes nothing.

**HOST:** And there's a second half — the rowcount guard. After B's write does nothing, the code checks "how many rows did I just change? Zero? Then raise an error." Why is *that* needed? Isn't the "if" enough?

**MERCED:** The if stops B from *writing*. The rowcount guard stops B from *believing it won*. Without it, B's code continues down the completion path — sends messages, charges credits — convinced it owns the close. The guard converts a silent no-op into a loud failure: "you lost the race, stop."

**HOST:** And this, you told me, retroactively answered a question you'd fumbled days earlier: why does the one-active-conversation rule live in the *database* as a constraint, rather than as a check in the Python code?

**MERCED:** Because a check in Python is two moments again — check, then act — and time passes between them. But a constraint at the database boundary is enforced at the single point where data is actually written, where the database's one-writer-at-a-time rule protects it. The invariant lives where it can't be raced. Python checks are for friendly error messages; database constraints are for truth.

**HOST:** Let's do the retention part honestly, because that's the experiment you're running on yourself. Five days after hearing these ideas passively, you retained zero of five concepts. But idempotency — which you coined a shape for yourself, forgot completely after one day, and had re-presented — you recalled cold, unaided, days later. In your own words?

**MERCED:** "One run or fifty runs — same final outcome." If the charge record already exists, the retry sees it and skips. That's the keyed trick: make the retry harmless by giving the operation a memory of itself.

**HOST:** And the difference between forgetting it at day one and recalling it at day five wasn't intelligence —

**MERCED:** It was whether I'd been forced to produce it once in between. Retrieval is the rep. Hearing is not.

**HOST:** Last question, the transfer test — listeners, play along. A wallet: users have credits, a spend operation checks "is the balance above zero" and then deducts. Three concurrent requests, one credit left. What's the guarded write, in plain words?

... ... ...

**MERCED:** "Spend one credit *if* the balance is greater than zero" — one operation, checked by rowcount. And I'll tell you honestly: I got this right on my second try, not my first, and I told the teacher I still wasn't confident. That lack of confidence after a correct answer is what a *first landing* feels like. It's not mastery. It's the sign that the recall check in three days is the real test.

**HOST:** Which is the through-line of everything you've built here: the confidence you feel at the end of a lesson is not evidence. The evidence is what survives the delay. Merced, thanks for walking us through it.

**MERCED:** Thanks for the pauses. Answer them for real next time — the pause is the rep.
