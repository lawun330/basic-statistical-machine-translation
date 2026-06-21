import streamlit as st

from config import DIRECTIONS
from decoder import MosesDecodeError, translate_line
from normalize import normalize_myanmar_line

st.set_page_config(
    page_title="Burmese G2P SMT",
    page_icon="🌐",
    layout="wide",
)

PANEL_HEIGHT = 120

st.markdown(
    """
<style>
    div[data-testid="stVerticalBlock"]:has(> div.swap-btn-wrap) {
        justify-content: center;
    }
    div.swap-btn-wrap button[kind="secondary"] {
        border-radius: 50%;
        width: 2.75rem;
        height: 2.75rem;
        min-height: 2.75rem;
        padding: 0;
        font-size: 1.25rem;
        line-height: 1;
        border: 1px solid rgba(49, 51, 63, 0.2);
    }
    div.swap-btn-wrap button[kind="secondary"]:hover {
        background: rgba(49, 51, 63, 0.08);
    }
    div.panel-header {
        min-height: 2.5rem;
    }
</style>
""",
    unsafe_allow_html=True,
)

st.title("Burmese Grapheme and Phoneme Translator")

if "direction" not in st.session_state:
    st.session_state.direction = "my-ph"


def clear_all() -> None:
    st.session_state.input_text = ""
    st.session_state.output_text = ""
    st.session_state.pop("last_output", None)
    st.session_state.pop("last_direction", None)
    st.session_state.pop("last_normalized", None)


direction = st.session_state.direction
meta = DIRECTIONS[direction]

if direction == "my-ph":
    source_label, target_label = "Grapheme", "Phoneme"
else:
    source_label, target_label = "Phoneme", "Grapheme"

if "input_text" not in st.session_state:
    st.session_state.input_text = ""

if "output_text" not in st.session_state:
    st.session_state.output_text = ""

if st.session_state.get("last_direction") == direction:
    st.session_state.output_text = st.session_state.get("last_output", "")
else:
    st.session_state.output_text = ""

col_in, col_swap, col_out = st.columns([11, 1, 11], vertical_alignment="top")

with col_in:
    st.subheader(source_label)
    text = st.text_area(
        "Input",
        height=PANEL_HEIGHT,
        placeholder=meta["placeholder"],
        help=meta["help"],
        key="input_text",
        label_visibility="collapsed",
    )
    translate_btn = st.button("Translate", type="primary", use_container_width=True)

with col_swap:
    st.markdown('<div class="panel-header">&nbsp;</div>', unsafe_allow_html=True)
    st.markdown('<div class="swap-btn-wrap">', unsafe_allow_html=True)
    swap = st.button(
        "⇄",
        key="swap_direction",
        help="Swap translation direction",
        use_container_width=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)

with col_out:
    st.subheader(target_label)
    st.text_area(
        "Output",
        height=PANEL_HEIGHT,
        disabled=True,
        label_visibility="collapsed",
        key="output_text",
    )
    st.button("Clear", use_container_width=True, on_click=clear_all)

if swap:
    has_input = bool(text.strip())
    has_output = bool(
        st.session_state.get("last_direction") == direction
        and st.session_state.get("last_output", "").strip()
    )
    if has_input or has_output:
        st.warning("Please click **Clear** before swapping direction.")
    else:
        st.session_state.direction = "ph-my" if direction == "my-ph" else "my-ph"
        st.session_state.pop("last_output", None)
        st.session_state.pop("last_direction", None)
        st.session_state.pop("last_normalized", None)
        st.rerun()

if translate_btn:
    if not text.strip():
        st.warning("Enter some text first.")
    else:
        try:
            prepared = text.strip()
            if meta["normalize"]:
                prepared = normalize_myanmar_line(prepared)
                st.session_state["last_normalized"] = prepared

            result = translate_line(prepared, meta["config"])
            st.session_state["last_output"] = result
            st.session_state["last_direction"] = direction
            st.rerun()
        except MosesDecodeError as exc:
            st.error(f"Decode failed:\n\n{exc}")

if (
    st.session_state.get("last_direction") == direction
    and st.session_state.get("last_output")
    and meta["normalize"]
    and st.session_state.get("last_normalized")
):
    with st.expander("Normalized input (sent to Moses)"):
        st.code(st.session_state["last_normalized"])

with st.expander("Model info"):
    st.markdown(
        f"""
- **Model**: `SMT run6 (run8 in pbsmt_v4 => baseline2/run5)`
- **Experiment**: `new syl-normalization, 3-gram, max-phrase 3, prune 001, MGIZA`
- **Decoder**: `moses decoder from moses-release/RELEASE-4.0/binaries`
- **Direction**: `{direction}`
- **Config**: `{meta['config']}`
"""
    )
