from typing import Optional, Tuple, List
import gradio

import facefusion.globals
import facefusion.choices
from facefusion import wording
from facefusion.typing import FaceMaskType, FaceMaskRegion
from facefusion.uis.core import register_ui_component

FACE_MASK_TYPES_CHECKBOX_GROUP : Optional[gradio.CheckboxGroup] = None
FACE_MASK_BLUR_SLIDER : Optional[gradio.Slider] = None
FACE_MASK_BOX_GROUP : Optional[gradio.Group] = None
FACE_MASK_REGION_GROUP : Optional[gradio.Group] = None
FACE_MASK_PADDING_TOP_SLIDER : Optional[gradio.Slider] = None
FACE_MASK_PADDING_RIGHT_SLIDER : Optional[gradio.Slider] = None
FACE_MASK_PADDING_BOTTOM_SLIDER : Optional[gradio.Slider] = None
FACE_MASK_PADDING_LEFT_SLIDER : Optional[gradio.Slider] = None
FACE_MASK_REGION_CHECKBOX_GROUP : Optional[gradio.CheckboxGroup] = None


def render() -> None:
  pass

def listen() -> None:
  pass

def update_face_mask_type(face_mask_types : List[FaceMaskType]) -> Tuple[gradio.CheckboxGroup, gradio.Group, gradio.CheckboxGroup]:
	if not face_mask_types:
		face_mask_types = facefusion.choices.face_mask_types
	facefusion.globals.face_mask_types = face_mask_types
	has_box_mask = 'box' in face_mask_types
	has_region_mask = 'region' in face_mask_types
	return gradio.CheckboxGroup(value = face_mask_types), gradio.Group(visible = has_box_mask), gradio.CheckboxGroup(visible = has_region_mask)


def update_face_mask_blur(face_mask_blur : float) -> None:
	facefusion.globals.face_mask_blur = face_mask_blur


def update_face_mask_padding(face_mask_padding_top : int, face_mask_padding_right : int, face_mask_padding_bottom : int, face_mask_padding_left : int) -> None:
	facefusion.globals.face_mask_padding = (face_mask_padding_top, face_mask_padding_right, face_mask_padding_bottom, face_mask_padding_left)


def update_face_mask_regions(face_mask_regions : List[FaceMaskRegion]) -> gradio.CheckboxGroup:
	if not face_mask_regions:
		face_mask_regions = facefusion.choices.face_mask_regions
	facefusion.globals.face_mask_regions = face_mask_regions
	return gradio.CheckboxGroup(value = face_mask_regions)
