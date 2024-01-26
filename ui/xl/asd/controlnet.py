import ipywidgets as widgets
from IPython.display import display, HTML, clear_output
from gutris1 import download

bura = "/home/studio-lab-user/asd/asd/controlnet.css"
with open(bura, "r") as oppai:
    susu = oppai.read()
display(HTML(f"<style>{susu}</style>"))
    
url_list = {
    "https://huggingface.co/lllyasviel/sd_control_collection/resolve/main/diffusers_xl_canny_mid.safetensors \
    diffusers_xl_canny_mid.safetensors": "Diffusers XL Canny Mid",
    "https://huggingface.co/lllyasviel/sd_control_collection/resolve/main/diffusers_xl_depth_mid.safetensors \
    diffusers_xl_depth_mid.safetensors": "Diffusers XL Depth Mid",
    
    "https://huggingface.co/lllyasviel/sd_control_collection/resolve/main/kohya_controllllite_xl_blur.safetensors \
    kohya_controllllite_xl_blur.safetensors": "Kohya Controlite XL Blur",
    "https://huggingface.co/lllyasviel/sd_control_collection/resolve/main/kohya_controllllite_xl_blur_anime.safetensors \
    kohya_controllllite_xl_blur_anime.safetensors": "Kohya Controlite XL Blur Anime",
    "https://huggingface.co/lllyasviel/sd_control_collection/resolve/main/kohya_controllllite_xl_canny.safetensors \
    kohya_controllllite_xl_canny.safetensors": "Kohya Controlite XL Canny",
    "https://huggingface.co/lllyasviel/sd_control_collection/resolve/main/kohya_controllllite_xl_canny_anime.safetensors \
    kohya_controllllite_xl_canny_anime.safetensors": "Kohya Controlite XL Canny Anime",
    "https://huggingface.co/lllyasviel/sd_control_collection/resolve/main/kohya_controllllite_xl_depth.safetensors \
    kohya_controllllite_xl_depth.safetensors": "Kohya Controlite XL Depth",
    "https://huggingface.co/lllyasviel/sd_control_collection/resolve/main/kohya_controllllite_xl_depth_anime.safetensors \
    kohya_controllllite_xl_depth_anime.safetensors": "Kohya Controlite XL Depth Anime",
    "https://huggingface.co/lllyasviel/sd_control_collection/resolve/main/kohya_controllllite_xl_openpose_anime.safetensors \
    kohya_controllllite_xl_openpose_anime.safetensors": "Kohya Controlite XL Openpose Anime",
    "https://huggingface.co/lllyasviel/sd_control_collection/resolve/main/kohya_controllllite_xl_openpose_anime_v2.safetensors \
    kohya_controllllite_xl_openpose_anime_v2.safetensors": "Kohya Controlite XL Openpose Anime V2",
    "https://huggingface.co/lllyasviel/sd_control_collection/resolve/main/kohya_controllllite_xl_scribble_anime.safetensors \
    kohya_controllllite_xl_scribble_anime.safetensors": "Kohya Controlite XL Scribble Anime",

    "https://huggingface.co/lllyasviel/sd_control_collection/resolve/main/t2i-adapter_xl_canny.safetensors \
    t2i-adapter_xl_canny.safetensors": "T2I Adapter XL Canny",
    "https://huggingface.co/lllyasviel/sd_control_collection/resolve/main/t2i-adapter_xl_openpose.safetensors \
    t2i-adapter_xl_openpose.safetensors": "T2I Adapter XL Openpose",
    "https://huggingface.co/lllyasviel/sd_control_collection/resolve/main/t2i-adapter_xl_sketch.safetensors \
    t2i-adapter_xl_sketch.safetensors": "T2I Adapter XL Sketch",
    "https://huggingface.co/lllyasviel/sd_control_collection/resolve/main/t2i-adapter_diffusers_xl_canny.safetensors \
    t2i-adapter_diffusers_xl_canny.safetensors": "T2I Adapter Diffusers XL Canny",
    "https://huggingface.co/lllyasviel/sd_control_collection/resolve/main/t2i-adapter_diffusers_xl_depth_midas.safetensors \
    t2i-adapter_diffusers_xl_depth_midas.safetensors": "T2I Adapter Diffusers XL Depth Midas",
    "https://huggingface.co/lllyasviel/sd_control_collection/resolve/main/t2i-adapter_diffusers_xl_depth_zoe.safetensors \
    t2i-adapter_diffusers_xl_depth_zoe.safetensors": "T2I Adapter Diffusers XL Depth Zoe",
    "https://huggingface.co/lllyasviel/sd_control_collection/resolve/main/t2i-adapter_diffusers_xl_lineart.safetensors \
    t2i-adapter_diffusers_xl_lineart.safetensors": "T2I Adapter Diffusers XL Lineart",
    "https://huggingface.co/lllyasviel/sd_control_collection/resolve/main/t2i-adapter_diffusers_xl_openpose.safetensors \
    t2i-adapter_diffusers_xl_openpose.safetensors": "T2I Adapter Diffusers XL Openpose",
    "https://huggingface.co/lllyasviel/sd_control_collection/resolve/main/t2i-adapter_diffusers_xl_sketch.safetensors \
    t2i-adapter_diffusers_xl_sketch.safetensors": "T2I Adapter Diffusers XL Sketch",

    "https://huggingface.co/h94/IP-Adapter/resolve/main/sdxl_models/ip-adapter_sdxl.safetensors \
    ip-adapter_sdxl.safetensors": "IP Adapter SDSXL",
    "https://huggingface.co/h94/IP-Adapter/resolve/main/sdxl_models/ip-adapter_sdxl_vit-h.safetensors \
    ip-adapter_sdxl_vit-h.safetensors": "IP Adapter SDSXL VIT-H",
    "https://huggingface.co/h94/IP-Adapter/resolve/main/sdxl_models/ip-adapter-plus-face_sdxl_vit-h.safetensors \
    ip-adapter-plus-face_sdxl_vit-h.safetensors": "IP Adapter Plus Face SDSXL VIT-H",
    "https://huggingface.co/h94/IP-Adapter/resolve/main/sdxl_models/ip-adapter-plus_sdxl_vit-h.safetensors \
    ip-adapter-plus_sdxl_vit-h.safetensors": "IP Adapter Plus SDSXL VIT-H",
    "https://huggingface.co/h94/IP-Adapter-FaceID/resolve/main/ip-adapter-faceid-plusv2_sdxl.bin \
    ip-adapter-faceid-plusv2_sdxl.bin": "IP Adapter FaceID Plusv2"
}

list_half = len(url_list) // 2
half_list_1 = dict(list(url_list.items())[:list_half])
half_list_2 = dict(list(url_list.items())[list_half:])

cb1 = widgets.VBox(
    [widgets.Checkbox(
        value=False,
        description=name,
        style={'description_width': '0px'})
    for url, name in half_list_1.items()])
cb1.add_class("checkbox-group1")

cb2 = widgets.VBox(
    [widgets.Checkbox(
        value=False,
        description=name,
        style={'description_width': '0px'})
    for url, name in half_list_2.items()])
cb2.add_class("checkbox-group2")

db = widgets.Button(description="Download")
db.add_class("download-button")
dbo = widgets.Output()
cbc = widgets.HBox([cb1, cb2], layout=widgets.Layout(align_items='flex-start'))

def sa_cb(b):
    for checkbox in cb1.children + cb2.children:
        checkbox.value = True

def usa_cb(b):
    for checkbox in cb1.children + cb2.children:
        checkbox.value = False
        
sab = widgets.Button(description="Select All")
sab.add_class("select-all-button")
sab.on_click(sa_cb)

usab = widgets.Button(description="Unselect All")
usab.add_class("unselect-all-button")
usab.on_click(usa_cb)

bs = widgets.Button(description="")
bs.add_class("border-style")

bl = widgets.HBox([sab, usab, db, bs])
boks = widgets.VBox([bl, cbc])
boks.layout.width = '630px'
boks.layout.height = '455px'
boks.layout.padding = '0px'
boks.add_class("boks")
display(boks)
        
def d_b_click(b):
    selected_urls = [
        url 
        for checkbox, (url, name) in zip(cb1.children + cb2.children, url_list.items()) 
        if checkbox.value
    ]
    widgets.Widget.close(boks)
    with dbo:
        for url in selected_urls:
            download(url)
            
display(dbo)
db.on_click(d_b_click)