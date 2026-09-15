# CapCut execution and delivery

Read only after the current flow is approved. This documents a working macOS route, not an official CapCut API or a guarantee for every version.

## Capability check

- Verify CapCut desktop is installed and accessible to the host's computer-use tools. Inspect actual UI state before actions. The successful environment used `cua_repl`; other hosts may expose a different approved control surface.
- Use a genuine CapCut connector if one exists. ChatCut is a different editor.
- When no control surface is available, stop at the approved plan and state what is missing. Installing this skill does not grant UI access.
- Local Python/FFmpeg/Whisper are useful for analysis and verification. They do not replace the requested editor without the user's agreement.

## Preferred UI route

1. Create a new task-owned project per version, import the original video and place it on the main track.
2. Split/trim original clips according to the approved source-time map. Move clips in the approved order, keeping linked audio with video.
3. Confirm the first clip is the approved hook and the second is the full signature-plus-English span.
4. Close gaps, preserve natural speech joins and remove duplicated moved sentences.
5. Verify no text, music, graphics, voiceover or effect tracks were added for flow-only delivery.
6. Save, reopen/preview the actual project, export locally and inspect the exported file.

Do not reuse screen coordinates from another session. Native accessibility labels can group several menu items; when a click does not work, inspect the new screenshot/state before retrying. Export progress is not completion; wait for the app's saved-to-computer confirmation. Close the share screen without posting to TikTok/YouTube.

## Optional native-draft route: version-dependent

This was successfully used with readable JSON drafts on one Mac installation. It is an implementation option, not the skill's universal default. If the current app stores encrypted/unknown drafts, use the UI route; do not try to bypass encryption.

Only use it when all of these hold:
- The user has approved this exact flow.
- The source skeleton is a **new, task-owned, single-source project**, saved by the current CapCut build. It has no third-party asset dependencies or creative effects that must be preserved.
- CapCut is closed through the supported UI before writing; backups of all touched files and the project index are stored in the task folder.
- You can explain every changed field from inspected files. Never blindly run a template against another user's projects.

Discover the project directory from the current app's Details view. A previously observed layout was a `com.lveditor.draft` directory beneath the user's Movies folder, with:
- Root `draft_info.json` and `draft_meta_info.json`.
- `Timelines/project.json` identifying the active timeline.
- `Timelines/<timeline-id>/draft_info.json` containing timeline state.
- `root_meta_info.json` in the project parent directory, indexing projects.

Confirm the actual layout before using it. Some builds use different filenames. Do not hardcode usernames, project IDs, existing project names or source paths.

### Fields to preserve or update deliberately

- Copy the current project's full video material and segment structures, preserving media references and version/configuration metadata.
- Use a fresh project/timeline/track/segment identity for an independently created project. Keep registry and path references consistent, and preserve every unrelated index entry.
- Each segment has a `source_timerange` and `target_timerange`, commonly in microseconds. Derive from frame counts using the source FPS; compute target start from cumulative frames to avoid accumulated rounding gaps.
- Trim and reorder the original linked video/audio. Update total duration and metadata in all authoritative copies identified from the current build.
- Use one video track for this flow-only case. Do not introduce text materials or effects. Do not erase effects from unrelated or user-created existing projects.
- Never remove extra material references just to make validation pass. If a referenced object is required, preserve it; otherwise verify the reference is unused before omission.
- The app may prefer timeline copies over root copies, or use temporary snapshots. Confirm what it actually loads. Archive only task-owned stale snapshots with a backup; don't clear global caches.
- Reopen the project through CapCut. The displayed clip count, duration, hook and brand segment must match the approved plan before exporting.

Stop this route after one schema mismatch or failed reopen, restore only the files changed by this task, and fall back to UI editing. Do not repeatedly rewrite indexes speculatively. Do not restore an old whole index over newly created user projects.

## Cut quality

Whisper's word boundaries are estimates. Inspect/listen to the source around each join. Silence detection can help locate breath spaces but is not an automatic instruction to remove every pause. Preserve the emotional pause before a payoff where it contributes meaning.

Use complete speech units. A rewritten review sentence is not permission to synthesize new audio. If the approved meaning cannot be assembled from recorded words, identify the specific missing line before editing that portion.

## Export and verification

Prefer H.264 MP4 at original frame rate/aspect ratio. Keep the source resolution unless an export requirement says otherwise. CapCut's 1080p export of 720p footage is an upscale, not extra original detail.

If the app exports H.264 MOV, a lossless container conversion is valid after the actual CapCut export:

```sh
ffmpeg -i 'CapCut-export.mov' -map 0:v:0 -map 0:a:0 -c copy -movflags +faststart 'Version_A.mp4'
```

Check file metadata and decode the whole file:

```sh
ffmpeg -hide_banner -i 'Version_A.mp4' -f null -
```

Inspect/listen to the output's opening, each new join and ending; verify approved order and no added text. Report what was actually verified. Audio-envelope comparison can establish that exported segments correspond to selected source ranges; raw AAC waveform differences alone do not establish a bad cut.

Final handoff: two MP4s, their durations, two editable project locations and `edit-plan.json`/approval record. Do not call an export complete merely because a filename is present while rendering is still in progress.
