# ONE (Switch Demo) 解包记录
## 整体
看起来就是Unity的外层封包，实际上也是。AssetStudio打开单个文件即可。注意不要选Load Folder，会报错。  
Options - Export options 取消勾选 Convert Texture2D 和 Convert AudioClip to WAV(PCM)  
## 视频
打开movie，直接提取其中文件即可。  
MP4 isom (isom/iso2/avc1/mp41)/AVC 1920\*1080 8bits 30.0FPS/AAC LC 48.0kHz/overall bit rate 15.7Mbps  
MP4 mp42 (mp42/mp41)/AVC 1920\*1080 8bits 29.970FPS/AAC LC 48.0kHz/overall bit rate 21.5Mbps  
## 图片
测试了 image_bg image_ev，包内看起来使用了atx扩展名，实际使用了PK文件头，可用GARBro将其作为压缩包打开。  
其中包含一个atlas.json和一个atlas.pb文件，以及若干个webp文件。  
webp文件没有加密，可直接读取，但其上有透明缝隙——即图片看起来是由约256\*256的小块拼凑的。这些小块有效部分为250\*250，边缘包含1像素的透明缝隙和2像素的边缘拖影。  
脚本已完成，支持立绘(bustup)，勉强支持system。  
## 脚本
竟然是明文存储。  
## 音频
Unity传统OGG Xiph.Org libVorbis，标准文件头。  
OGG/Vorbis lossy 48kHz/465~160kbps  
## Emote
我看不懂。  
emote文件可以解出来一大堆东西，其中\*.psz和相应的\*_tex000应该是一对，psz文件可以用FreeMote解压缩，得到一个巨大的json文件。有些psz文件在文件头前有内容，需要手动删除才能被FreeMote提取。至于tex文件，我看着像没有文件头的DXT1，不过不对。AssetStudio认为是BC7格式的图片，并给出了解读，但也完全不成样子，颜色似乎有点那意思。如果把横向长度裁剪到一半或四分之一，可能可以看出来一点，还需要进一步尝试。  
[FreeMote wiki PSZ](https://github.com/UlyssesWu/FreeMote/wiki/PSB-Shells,-Types,-Platforms#psz)  