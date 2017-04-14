# ocr-api

> 2017年3月23日 苹果收购知名效率应用 workflow

### 前言

有几次淘宝退货，需要获取交易单号，但淘宝客户端不能复制单号，我只能背下来，或者抄下来，再在退货页面填下，效率极其低下。

得知 workflow 免费，赶紧下了一个来体验，体验过程中想到了这个问题，进而用 django 写下了这个图片识别接口，供 workflow 调用

### 安装

安装 tesseract

安装 tesseract 中文包

mac:

```
brew install tesseract
```

安装依赖
```
pip install -r requirements.txt
```

配置 django


完成上面的工作之后，在浏览器打开 

```
http://localhost/upload/
```

上传一张图片，然后你会得到图片上的文字

目前中文识别比较差，数字的还行

如果把 tesseract 识别语言设为中文的话，英文的识别率就非常低了，不然英文的识别率还挺高
