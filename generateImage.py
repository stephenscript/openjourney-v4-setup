from diffusers import DiffusionPipeline
# load pre-trained model
pipe = DiffusionPipeline.from_pretrained("./openjourney-v4")

# significantly improves performance
pipe = pipe.to("mps")

# Recommended for machines with less than 64GB of RAM
pipe.enable_attention_slicing()

# define prompt text
prompt = "infinity frog"

# generate image from prompt
img = pipe(prompt).images[0]
img.save("./" + prompt + ".jpg")
