# Openjourney-v4 Local Setup

## About

This is a simplified setup of the Open Journey v4 image generation model available on [huggingface](https://huggingface.co/prompthero/openjourney-v4). It allows you to start creating AI-generated images on your local machine.
## Setup

There's a bit of setup required for this repo so buckle up.

If you don't have [brew](https://brew.sh/) or [python3](https://docs.brew.sh/Homebrew-and-Python) installed you're gonna have a bad time. Get that set up before continuing.

Next order of business, you're going to need [git-lfs](https://git-lfs.com) to manage exceedingly large files associated with the OpenJourney repo:

```bash
brew install git-lfs
```

Then run the following commands in this repo's directory to clone the OpenJourney model:

```bash
git lfs install
git clone https://huggingface.co/prompthero/openjourney-v4
```

Fair warning, the files exceed 25GB and will take a while to pull down. If you want to clone without large files and just have reference to their pointers, prepend the git clone with:

```yaml
GIT_LFS_SKIP_SMUDGE=1
```

Now you're going to need a few more dependencies to make the magic happen:

```bash
# diffusers library
pip3 install diffusers
# pytorch
pip3 install torch
```

## Usage

Once setup is complete, update the prompt in generateImage.py run the following command:

```bash
python3 generateImage.py
```

An image will be created using the OpenJourney-v4 image generation model. Enjoy!

## Disclaimer

***Please note this setup is geared towards MacBooks with Apple Silicon chips. Performance may vary for other setups***

## About

If you found this setup tutorial useful or had any issues along the way, feel free to contact me at stephen.anthony.rivas@gmail.com or hit me up on [LinkedIn](https://linkedin.com/in/stephenpharmd). Also if you create any amusing images please send them my way, I'd love to see them!