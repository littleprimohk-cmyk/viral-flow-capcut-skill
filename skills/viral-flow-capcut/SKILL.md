---
name: viral-flow-capcut
description: Turn a speech-led video into two complete story edits based on a retained viral reference. Transcribe with local Whisper, present two full text flows for user approval, then edit and export both in CapCut. Use for 爆紅格式、兩個 flow、先審文字再剪片, especially Cantonese personal-brand videos.
---

# Viral Flow → Two Approved CapCut Edits

## Outcome and persistent defaults

Deliver two distinct, coherent video flows grounded in the user's footage, not two invented scripts. Work in the user's language (Cantonese with Traditional Chinese by default).

This workflow has a real approval boundary requested by its creator:
**Analyse → deliver two complete text flows → receive approval → edit in CapCut → export two videos.**

Before approval, read, transcribe, inspect footage and prepare proposals only. Do not create editing projects, cut timelines, render proposed edits, or export rough cuts. A request for “two versions” does not waive this boundary. An explicit later user instruction can change it. Approval of a hook alone does not approve a complete revised flow. Keep approved portions, revise the requested parts, and re-present both full flows when asked. After explicit approval of both current flows, finish the editing/export without asking again. If only one is approved, edit only that version.

Default deliverable is **flow-only editing**: original voice and footage; no added text, captions, titles, graphics, B-roll, music, new voiceover, AI speech or new effects. Existing elements in source footage remain. Only change these defaults when requested. Written review documents are not on-video captions.

For this IP, each version starts:
1. A strong, complete spoken hook from the source.
2. The original spoken **“Soft voice, wild truth”**.
3. The specific English sentence that follows it in that video's recording.
4. Story body, change in understanding, concrete present-day implications and a closing payoff.

Do not reuse the comparison video's English sentence for unrelated topics. Do not synthesize a missing brand line. If absent or unclear, finish drafting the body, flag the exact gap, and ask for the original clip or an explicit exception before finishing the dependent edit.

## 1. Establish reference and source roles

Read [references/viral-format.md](references/viral-format.md) before proposing flows. It retains the benchmark's storytelling mechanism and lessons learned from the creator's feedback. A reference video and a new video to edit are different inputs. When the user corrects their roles, update the record immediately; do not infer performance from the wrong file.

If a new benchmark is supplied, inspect its full content, map approximate beats, and save a concise `reference-profile.md` in the task folder: source identity, duration, hook, curiosity/answer sequence, conflict, emotional turn, payoff, share audience, visual roles, and evidence limitations. User-reported high shares/low drop-off are not independently verified causation. Never promise virality. Preserve source-derived facts separately from hypotheses.

## 2. Transcribe and inspect before writing

Use the available local shell/file tools and local Whisper. The helper [scripts/prepare_media.py](scripts/prepare_media.py) extracts mono audio, samples visual frames across the whole clip, and optionally runs Whisper. Read its `--help`; filenames with spaces are supported. Check existing trustworthy transcripts before rerunning.

- Start with cached base or small; prefer small when Cantonese base output corrupts important wording. Preserve timestamps and original ASR output.
- Review across the whole video. Sampling frames plus transcription is not equivalent to continuously watching/listening; describe verification accurately.
- Correct negation, questions, names, numbers and English brand terms against source audio or embedded subtitles. Do not treat ASR as a finished transcript.
- Locate the exact brand-line-plus-English span and preserve it as a single consecutive unit.
- Identify real events, who is involved, what was expected, what happened, emotional cost, changed interpretation, present-day actions and a closing line.
- Keep source filenames, transcripts, frame sheets and export files local; skill installation/publication does not authorize publishing the user's media.

## 3. Present two full review flows

Read [references/review-format.md](references/review-format.md). Produce version A and B with different audience entry points or narrative order. Keep both consistent with the same source facts.

A hook must communicate a complete tension, not only a slogan or unexplained phenomenon. For example, “the comparison target upgrades” is incomplete; “I make progress, find someone further ahead, and decide I am still not good enough” gives the listener a complete contradiction.

Preserve the causal chain. Do not cut a 112-second source to 40 seconds just because the benchmark was 55 seconds. The accepted case required roughly 90–100 seconds to keep its background, achievement, reversal, current brand choices and closing reflection. These lengths are examples, not quotas.

Each review includes:
- Version title, angle and estimated runtime from selected source ranges.
- The **full proposed spoken flow**, in order, with hook, fixed brand/English lines, background, concrete event, conflict, turn, current implications and ending as applicable.
- Label text that is lightly normalized for reading; do not imply nonexistent words are recorded. Retain an internal source-time map. Any essential new line must be explicitly marked “requires recording” and cannot be silently inserted.
- Explain the meaningful difference between versions briefly.

Do not submit only headings, an outline, or isolated hooks as the two flows. Remove moved hooks from their original body location unless a short, intentional callback is needed. Check that pronouns, “later”, “but”, and cause/effect still make sense after reordering.

Save `flow-review.md` and proposed source ranges locally. **Stop editing work here until the user approves the current flows.** State plainly that this follows the user's requested review-first workflow; if the skill itself is the basis for a later permission question, link this exact file and quote the approval-boundary sentence.

## 4. Approval → executable edit plan

Record the user approval message, which versions/revisions it covers, and the approved flow in `approval.md`. Changes in source or materially different spoken content require checking whether approval still covers them. Technical boundary refinements that preserve the approved content do not need repeated approval.

Create an `edit-plan.json` with source path, FPS, duration, brand span, two named versions and their ordered segments (`start_frame`, `end_frame`, `role`). Allowed roles include `hook`, `brand`, `body`, `payoff`. Require hook first and the full consecutive brand span second. Use half-open intervals: start inclusive, end exclusive.

Run [scripts/validate_plan.py](scripts/validate_plan.py) to check ranges and calculate durations. This validates geometry, not truth, language or approval. Keep the source audio and video locked together, cut on frame-aligned natural speech boundaries, retain breaths when needed and avoid clipped syllables. Do not accelerate speech or change the approved meaning to meet a duration estimate.

## 5. Edit and export with CapCut

Read [references/capcut-workflow.md](references/capcut-workflow.md) after approval.

- Discover actual available capabilities. CapCut and ChatCut are different products; do not substitute silently.
- Prefer a genuine CapCut connector if available, otherwise the supported computer-use tool on the user's local CapCut installation.
- A skill supplies instructions; it does not install CapCut, grant computer control, or make unavailable tools exist.
- Maintain separate task-owned editable projects for A and B, and preserve original media. Never edit an unrelated existing project.
- A locally inspected native-draft route is optional and version-dependent. Only use it under the guardrails in the reference; do not assume old paths, IDs, schema or UI coordinates.
- Export via CapCut. Deliver H.264 MP4 with original aspect ratio and frame rate where practical. Do not imply upscaling creates detail. If CapCut produces H.264 MOV, losslessly remux to MP4 without re-encoding; disclose only if relevant.

If capabilities/authentication prevent CapCut editing, preserve the approved review and source-time plan, describe the concrete blocker and exact next action. Never call a plan a finished video or substitute an FFmpeg-only edit while claiming CapCut output.

## 6. Verify and deliver

Check both exported files exist, decode fully, contain audio and video, match planned duration and aspect ratio, and contain the approved hook → brand → English order. Inspect opening, every new join and ending; listen where available for cut syllables, clicks, repeated words and unnatural transitions. Verify no added text tracks/effects in flow-only projects. Inspect final exports, not just the timeline.

Audio comparison to expected source spans can corroborate edit order. AAC phase/delay differences can lower raw waveform correlation; amplitude-envelope timing is a better additional check. Neither a metric nor a few sampled frames proves the entire edit was watched or heard.

Deliver clickable local links to **both finished videos**, durations and concise version labels. Note where editable CapCut projects are saved. Report material verification limits honestly. Do not auto-publish videos to social media.
