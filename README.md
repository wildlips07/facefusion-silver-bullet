top,small-large,large-small,best-worst,worst-best}  specify the order used for the face analyser
  --face-analyser-age {child,teen,adult,senior}                                                                      specify the age used for the face analyser
  --face-analyser-gender {male,female}                                                                               specify the gender used for the face analyser
  --face-detector-model {retinaface,yunet}                                                                           specify the model used for the face detector
  --face-detector-size {160x160,320x320,480x480,512x512,640x640,768x768,960x960,1024x1024}                           specify the size threshold used for the face detector
  --face-detector-score [0.0-1.0]                                                                                    specify the score threshold used for the face detector

face selector:
  --face-selector-mode {reference,one,many}                                                                          specify the mode for the face selector
  --reference-face-position REFERENCE_FACE_POSITION                                                                  specify the position of the reference face
  --reference-face-distance [0.0-1.5]                                                                                specify the distance between the reference face and the target face
  --reference-frame-number REFERENCE_FRAME_NUMBER                                                                    specify the number of the reference frame

face mask:
  --face-mask-types FACE_MASK_TYPES [FACE_MASK_TYPES ...]                                                            choose from the available face mask types (choices: box, occlusion, region)
  --face-mask-blur [0.0-1.0]                                                                                         specify the blur amount for face mask
  --face-mask-padding FACE_MASK_PADDING [FACE_MASK_PADDING ...]                                                      specify the face mask padding (top, right, bottom, left) in percent
  --face-mask-regions FACE_MASK_REGIONS [FACE_MASK_REGIONS ...]                                                      choose from the available face mask regions (choices: skin, left-eyebrow, right-eyebrow, left-eye, right-eye, eye-glasses, nose, mouth, upper-lip, lower-lip)

frame extraction:
  --trim-frame-start TRIM_FRAME_START                                                                                specify the start frame for extraction
  --trim-frame-end TRIM_FRAME_END                                                                                    specify the end frame for extraction
  --temp-frame-format {jpg,png}                                                                                      specify the image format used for frame extraction
  --temp-frame-quality [0-100]                                                                                       specify the image quality used for frame extraction
  --keep-temp                                                                                                        retain temporary frames after processing

output creation:
  --output-image-quality [0-100]                                                                                     specify the quality used for the output image
  --output-video-encoder {libx264,libx265,libvpx-vp9,h264_nvenc,hevc_nvenc}                                          specify the encoder used for the output video
  --output-video-quality [0-100]                                                                                     specify the quality used for the output video
  --keep-fps                                                                                                         preserve the frames per second (fps) of the target
  --skip-audio                                                                                                       omit audio from the target

frame processors:
  --frame-processors FRAME_PROCESSORS [FRAME_PROCESSORS ...]                                                         choose from the available frame processors (choices: face_debugger, face_enhancer, face_swapper, frame_enhancer, ...)
  --face-debugger-items FACE_DEBUGGER_ITEMS [FACE_DEBUGGER_ITEMS ...]                                                specify the face debugger items (choices: bbox, kps, face-mask, score)
  --face-enhancer-model {codeformer,gfpgan_1.2,gfpgan_1.3,gfpgan_1.4,gpen_bfr_256,gpen_bfr_512,restoreformer}        choose the model for the frame processor
  --face-enhancer-blend [0-100]                                                                                      specify the blend amount for the frame processor
  --face-swapper-model {blendswap_256,inswapper_128,inswapper_128_fp16,simswap_256,simswap_512_unofficial}           choose the model for the frame processor
  --frame-enhancer-model {real_esrgan_x2plus,real_esrgan_x4plus,real_esrnet_x4plus}                                  choose the model for the frame processor
  --frame-enhancer-blend [0-100]                                                                                     specify the blend amount for the frame processor

uis:
  --ui-layouts UI_LAYOUTS [UI_LAYOUTS ...]                                                                           choose from the available ui layouts (choices: benchmark, webcam, default, ...)
```


Documentation
-------------

Read the [documentation](https://docs.facefusion.io) for a deep dive.

marinhelalmazan@gmail.com





