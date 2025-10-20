# Natural Language Processing Final Project

The goal of this project is to analyze text using the log probabilities from large language models.

This project can be ran with `uv`. If not installed, `uv` can be downloaded with the following command ([ref uv getting started guide](https://docs.astral.sh/uv/getting-started/installation/)).

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

From here, the repository can be cloned and the uv environment synced.

```bash
git clone https://github.com/wkaisertexas/nlp-final
cd nlp-final
uv sync # installs and setup up python venv
```

Finally, Jupyter Lab can be used to run each notebook.

```bash
uv run jupyter lab
```

> [!NOTE]
> If running on the cs servers, follow these steps:
>
> Some notebooks download large models from Hugging Face. By default, this is `~/.cache/huggingface/hub/`. However, on the CS servers the 100 GB allocation limit can easily be overwritten. To remedy this, update the `HF_HUB_CACHE` environment variable to a project directory. While you are at it, might as well update your `UV_CACHE_DIR` to use the project directory as well. 
> ```bash
> export HF_HUB_CACHE=/p/cavalier/.cache/hf
> export UV_CACHE_DIR=/p/cavalier/.cache/uv
> ```

To use the cs servers, run 

```bash
ls ~/ssh
```

If you see no, keys you need to run `ssh-keygen` to generate a public and private key pair.

Otherwise, ssh-copy-id 
```bash
ssh-copy-id xbk6xm@portal.cs.virgnia.edu # replace with your username
```

After this, the following entry can be added to your `~/.ssh/config` to set up proxy jumps to the [gpu servers](https://www.cs.virginia.edu/computing/doku.php?id=compute_resources).

```
Host !portal.cs.virginia.edu *.cs.virginia.edu
    User xbk6xm
    ProxyJump portal.cs.virginia.edu
    PubkeyAuthentication yes
```
