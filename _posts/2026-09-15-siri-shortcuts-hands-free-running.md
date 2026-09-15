---
title: "Hey Siri, How's My Run? Hands-Free Running with Siri and Shortcuts"
description: "Every Siri phrase iRunning understands — start, pause, skip, finish, and hear your stats mid-run — plus how to build your own shortcuts in the Shortcuts app."
categories: [features]
date: 2026-09-15 09:00:00
image:
  path: /assets/images/blog/siri-conversation.png
  width: 1440
  height: 1304
---

Halfway through a hard rep is a terrible time to use a touchscreen. Your hands are sweaty, the phone is zipped into a belt, and your eyes should be on the path.

Starting with iRunning 1.2, you don't need to touch the phone at all. Siri can start your workout, pause it at a crossing, skip an interval, finish and save the run, and tell you exactly how you're doing. Nothing to set up: install the app and the phrases just work.

<figure class="post-figure">
  <picture>
    <source media="(max-width: 560px)" srcset="{{ '/assets/images/blog/siri-conversation-mobile.png' | relative_url }}" width="800" height="1564">
    <img src="{{ '/assets/images/blog/siri-conversation.png' | relative_url }}" width="1440" height="1304" loading="lazy"
       alt="A run controlled by voice: start a run, announce my run, pause my run and finish my run, with what Siri and iRunning say back to each">
  </picture>
  <figcaption>A whole run, start to finish, without touching the phone.</figcaption>
</figure>

## What you need

- **iOS 18 or later** and **iRunning 1.2 or later**
- **Siri turned on** (Settings › Apple Intelligence & Siri, or Settings › Siri on older iPhones)
- **Voice cues on** in iRunning (Settings › Run experience › Voice cues). Your stats are read out by the same voice that calls your intervals, so if cues are off, Siri shows your stats on screen but you won't hear them.

Every phrase ends with **"in iRunning"**. That's how Siri knows which app you mean.

## During a run

These work with the phone locked, including from a pocket, a belt, or your AirPods.

| Say | What happens |
|---|---|
| "Siri, **announce my run** in iRunning" | Your current stats, spoken as one sentence |
| "Siri, **what's my pace** in iRunning" | Same full update |
| "Siri, **heart rate** in iRunning" | Same full update |
| "Siri, **pause my run** in iRunning" | Pauses the run. You'll hear *"Paused"* |
| "Siri, **resume my run** in iRunning" | Picks up where you left off. You'll hear *"Resumed"* |
| "Siri, **skip the interval** in iRunning" | Jumps to the next interval, just like the on-screen skip |
| "Siri, **finish my run** in iRunning" | Asks *"Finish this run?"*, then saves it |

A few details worth knowing:

- **Your update is one sentence.** By default it covers time left in the interval, heart rate and zone, pace, and distance. For example: *"1 minute 48 left in Run, heart rate 162, zone 4, target 155 to 168, pace 4:52 per kilometer, distance 2.4 kilometers."* Any number the app doesn't have yet, like heart rate without a Watch, is simply left out.
- **Finishing always asks first.** A misheard phrase won't end your long run at kilometer 18. The save covers everything a normal finish does: Apple Health, splits, and ending the Live Activity.
- **Skipping needs a moving run.** If you're paused, Siri will ask you to resume first. Skipping the last interval finishes the workout.
- **"Continue my run"**, **"End my run"**, and **"Next interval"** work too, if those come out more naturally mid-stride.

## Before and after a run

| Say | What happens |
|---|---|
| "Siri, **start a run** in iRunning" | Opens the app and starts your most recent workout |
| "Siri, **what's my workout today** in iRunning" | Today's session from your training plan, e.g. *"Today: Easy run + strides, week 3."* |
| "Siri, **what was my last run** in iRunning" | Workout, when, distance, time, and pace |
| "Siri, **how much did I run this week** in iRunning" | Number of runs, total distance, and total time |

"Start a run" still goes through the usual countdown, so you have a moment to cancel if Siri started the wrong thing. On a rest day, "What's my workout today" tells you so, along with the day of your next session.

## Make it yours in the Shortcuts app

Siri's built-in phrases cover the basics. The **Shortcuts app** goes further: iRunning adds **10 actions** there that you can combine into your own shortcuts. Open Shortcuts, tap **+**, then **Add Action**, and search for **iRunning**.

A few ideas to start with:

- **Name your favorite workout.** Add the **Start a run** action, tap **Workout**, and pick a specific session, like your Tuesday 400s. Name the shortcut "Track Tuesday". Now "Siri, Track Tuesday" starts exactly that workout, not just the last one you ran.
- **Turn auto-announce on and off with your voice.** **Toggle auto-announce** is only available in Shortcuts. It switches the regular announcements (every few minutes or every set distance) on or off and remembers your settings. Handy for race day, when you want updates every kilometer, and for easy runs, when you'd rather be left alone.
- **Put a run on your Home Screen.** Any shortcut can be added to the Home Screen as an icon: one tap and you're counting down.

## Make the update say what you care about

The sentence Siri triggers is fully customizable, and so is every other way you ask for stats. In iRunning, go to **Settings › Customise › Run screen › What to announce**:

- Pick **up to five things** to include and drag them into the order you want. Choose from time left, heart rate, pace, distance, total time, time to finish, average pace, zone, cadence, what's up next, and elevation gain.
- Turn on **Target band** to hear your target range right after heart rate or pace, e.g. *"target 155 to 168"*.
- Turn on **Up next** to hear what's coming, e.g. *"next, recover jog, 1 minute 30."*
- The **Sounds like** preview shows the sentence and roughly how long it takes to say, so you can keep it short enough to hear between breaths.

## Siri isn't always the right tool

Talking to Siri at threshold pace isn't for everyone, and a busy street can drown you out. For those runs, iRunning gives you the same update without saying a word:

- **The speaker button** on the run screen, and on your Live Activity on the Lock Screen and in the Dynamic Island
- **Holding the big number** on the locked run screen for a moment
- **The Action Button** on newer iPhones, for one press from your pocket. The setup takes a minute: see [how to put "Announce my run" on your iPhone's Action Button]({% post_url 2026-09-15-action-button-announce-my-run %}).

<figure class="post-figure">
  <picture>
    <source media="(max-width: 560px)" srcset="{{ '/assets/images/blog/no-siri-needed-mobile.png' | relative_url }}" width="800" height="932">
    <img src="{{ '/assets/images/blog/no-siri-needed.png' | relative_url }}" width="1440" height="1208" loading="lazy"
       alt="The iRunning run screen with the speaker button highlighted, and the locked run screen with the big countdown number highlighted">
  </picture>
  <figcaption>On the run screen, tap the speaker. On the locked screen, hold the big number.</figcaption>
</figure>

Put your headphones in, lock the phone, and run. When you want to know how it's going, just ask.
