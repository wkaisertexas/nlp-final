from IPython.display import display, HTML
import html
from transformers import AutoModelForCausalLM, AutoTokenizer

def token_hover_widget(tokenizer: AutoTokenizer, text: str, *, add_special_tokens=True):
    """Enables the however over a word and extract the token identifier"""
    # offsets are needed to map tokens back to the original text
    enc = tokenizer(
        text,
        return_offsets_mapping=True,
        add_special_tokens=add_special_tokens
    )

    ids = enc["input_ids"]
    offsets = enc["offset_mapping"]
    toks = tokenizer.convert_ids_to_tokens(ids)

    chips_html = []
    for i, (tok, (s, e), tid) in enumerate(zip(toks, offsets, ids)):
        # Some special tokens may have (0, 0) offsets; handle cleanly
        if s == e:
            tooltip = f"[SPECIAL] {tok} | idx={i}"
        else:
            substring = html.escape(text[s:e])
            tooltip = f"{substring} | {s}:{e} | idx={i}"

        # it would be nice if a t-string could be used here
        # TODO: replace Ġ with a " "
        tok = tok.replace("Ġ", " ")
        chip = f"""
        <span class="tok-chip" title="{tooltip}">
            {html.escape(tok)}
        </span>
        """
        chips_html.append(chip)

    style = """
    <style>
      .tok-wrap {{
        font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", monospace;
        line-height: 1.9;
        user-select: text;
      }}
      .tok-chip {{
        display: inline-block;
        margin: 2px 3px;
        padding: 2px 6px;
        border: 1px solid #ddd;
        border-radius: 6px;
        cursor: default;
        transition: background-color 120ms ease, box-shadow 120ms ease, border-color 120ms ease;
        white-space: pre; /* preserve leading 'Ġ' or '▁' etc. */
      }}
      .tok-chip:hover {{
        background: #f3f4f6;
        border-color: #bbb;
        box-shadow: 0 1px 3px rgba(0,0,0,0.06);
      }}
      .tok-legend {{
        color: #555;
        font-size: 0.9em;
        margin-bottom: 8px;
      }}
      .tok-legend code {{
        background: #f6f8fa;
        padding: 0 4px;
        border-radius: 4px;
      }}
    </style>
    """

    legend = """
    <div class="tok-legend">
      Hover a token to see: <em>substring</em> | <code>start:end</code> | <code>id</code>.
      Special tokens display as <code>[SPECIAL]</code>.
    </div>
    """

    html_block = f"""
    {style}
    <div class="tok-wrap">
      {legend}
      {''.join(chips_html)}
    </div>
    """

    display(HTML(html_block))