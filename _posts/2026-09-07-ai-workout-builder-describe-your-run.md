---
title: "Describe Your Run, Get a Workout: The AI Workout Builder on iPhone"
description: "Say \"6 × 400 m at 5K pace, 90 seconds rest\" and iRunning builds the intervals for you, on the phone, with Apple Intelligence. What it can do, where it stops, and how to get good results."
categories: [features]
date: 2026-09-07 09:00:00
image:
  path: /assets/images/blog/ai-flow.png
  width: 1440
  height: 744
---

Every runner has a workout in their head that they never quite get into an app. You know what you want: a warm-up, six fast 400s with a jog between them, a cool-down. Building that means a dozen taps: add block, set distance, set rest, repeat six times, name it.

iRunning has a shortcut. Tell it what you want in a sentence, and it builds the workout.

<figure class="post-figure">
  <picture>
    <source media="(max-width: 560px)" srcset="{{ '/assets/images/blog/ai-flow-mobile.png' | relative_url }}" width="800" height="1520">
    <img src="{{ '/assets/images/blog/ai-flow.png' | relative_url }}" width="1440" height="744" loading="lazy"
         alt="Three steps: describe the run in text or voice, Apple Intelligence on the iPhone builds the structure, and you get a normal iRunning workout with a warm-up, 6 × 400 m at 5K pace with 1:30 rests, and a cool-down, which you can save, edit or regenerate">
  </picture>
  <figcaption>A sentence in, a structured workout out. The model runs on the phone.</figcaption>
</figure>

## How it works

Open the **Workouts** tab and tap the **Describe your run** card (it's also a quick action on Home). Type a description, or tap the microphone and say it. Then **Generate workout**.

<figure class="post-figure">
  <picture>
    <source media="(max-width: 560px)" srcset="{{ '/assets/images/blog/ai-input-mobile.jpg' | relative_url }}" width="800" height="760">
    <img src="{{ '/assets/images/blog/ai-input.jpg' | relative_url }}" width="1440" height="920" loading="lazy"
         alt="The AI workout screen in iRunning: a text field that says Describe your run, a microphone button, four example chips such as 6 × 400m at 5K pace, 90s rest, and a Generate workout button">
  </picture>
  <figcaption>Type or dictate. The chips under the field are good starting points.</figcaption>
</figure>

A few seconds later you get a preview: the workout's name, its blocks and its total time. From there:

- **Save workout** puts it in My workouts, ready to start.
- **Edit** opens it in the regular builder, so you can change a rest, add a block or tighten a pace target.
- **Try again** regenerates from the same description.

The result is an ordinary iRunning workout. Voice cues, countdown beeps, targets and the Apple Watch all treat it exactly like one you built by hand.

## What it's good at

The model follows a few coaching rules, so its workouts have a sensible shape:

- **Warm-up and cool-down are added by default**, five easy minutes each, unless you say otherwise ("no warm-up, I'm already warm").
- **Repeats become repeat groups.** "8 × 200 m with 200 m jog" becomes a block that repeats eight times, with the work and the rest inside it.
- **Distances stay distances, times stay times.** "1 km" is measured by GPS; "90 seconds" is on the clock. Miles are converted.
- **It names the workout** with something short like "Tuesday 400s" or "Easy fartlek". You can rename it.

Descriptions that work well:

- *"Tempo run, 20 minutes at half-marathon pace"*
- *"Tabata: 8 × 20 seconds on, 10 seconds off"*
- *"Easy 5K with 4 strides at the end"*
- *"Pyramid: 1, 2, 3, 2, 1 minutes hard with equal rest"*
- *"10 × 1 minute fast, 1 minute walk, no cool-down"*

## Where it stops

- **It builds structure, not a plan.** It won't decide whether you should run 400s today; that's what training plans are for. It does exactly what you describe.
- **Pace targets are yours to set.** The model can label a block "5K pace", but the actual pace or heart-rate band is set in the builder, where the target uses your own zones.
- **Vague in, vague out.** "A hard run" gives you a generic session. Give it numbers: how many, how long, how much rest.
- **If it can't parse the description**, it says so and asks you to rephrase. It doesn't guess.

## Privacy, and what you need

Generation happens on the iPhone itself, using Apple Intelligence. Your description never leaves the device, and it works with no signal, in a stadium basement or on a plane.

That also sets the requirements:

- **iOS 26 or later** and an **iPhone that supports Apple Intelligence**, with Apple Intelligence turned on in Settings. On other phones the Describe your run card simply doesn't appear.
- **iRunning Premium.** The AI builder is part of the subscription. The regular workout builder, with two saved custom workouts, is free.
- Dictation uses the microphone and speech recognition, so iOS will ask for those permissions the first time you tap the mic.

## When to use it

The builder is faster when you're copying a structured session from a coach, a plan or a friend's message: read it out loud, tap Generate, check the preview, save. It's less useful for the free-form easy run, which is already one tap away as the **Free run** preset.

Try the one in your head. It's probably four words shorter than you think.
