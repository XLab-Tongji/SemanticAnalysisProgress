# EMOKIT调研文档

Author：郭辉 邹笑寒

[TOC]



## EMOKIT简介

EmoKit专注于研发情绪识别技术和内容匹配算法。通过融合体征分析、人体神经、数据挖掘、机器学习、物理分析等技术，将情绪识别引擎提供给开发者用户。通过本地SDK以及面向行业的自主研发产品形式，提供开放的情绪识别和内容匹配服务。

Emokit定位于情绪的识别、优化、表达。EmoKit通过分析用户的计步、心率、语音、笔迹等体征数据，并据此来判断用户的情绪、关联互联网内容。通过情感计算技术和最广泛的内容匹配算法，EmoKit将情感计算引擎提供给TO B 的企业和TO D 的开发者。

EmoKit通过提供本地SDK、云端API以及面向行业的自主研发产品形式，让情感计算技术在身边默默服务，让匹配的信息内容更加贴心。

####Emokit的三种形态：

* EmoKit-SDK，免费开放的情绪识别APT。目前合作案例有天天动听、咪咕音乐、体检宝等app，还有科大讯飞、环信等行业客户。SDK的用户数量已经超过1500万。
* EmoKit-IOT，免费硬件OS中的必备模块。这方面的应用有智能硬件、智能车载、智能家居。其中智能硬件合作案例有Google、海尔、英特尔等。
* EmoKit-EQ4AI，把EQ赋予人工智能。目前EmoKit已经与图灵机器人、UU机器人等建立了合作关系。让人工智能变得有情绪是AI 的发展趋势也是其难点所在。

####Emokit的应用领域

主要分四个领域：

* 移动互联网领域，它适用于很多app，是情绪识别的SDK(应用程序编程接口)；
* 在IOT(物联网)领域，它可以做到智能硬件操作系统里的必备模块，就像美国的苹果公司的homekit、healthkit等；
* 在人工智能领域，它是EQ4AI，就是把EQ赋予人工智能；
* 在很多行业里，他是针对特殊群体的情绪监测方案，比如针对呼叫中心坐席、针对学生、针对飞行员、针对司机等等。

#### Emokit的算法

从技术上来讲，算法精度的提升主要来自于两方面，专家模型和深度学习。

EmoKit情绪识别的大部分算法，是基于专家模型的，在此基础上再通过机器学习提升精度。人体一般在受到外界刺激时会产生情绪波动，这些波动，会通过人体的神经电，映射到我们的体征上，比如心率、皮电、语音等等，是可以被量化、识别、施加作用，并进行模拟的。这有别于普通人所认为情绪是模糊感性的，即唯心主义陷阱。

####EmoKit如何采集人的情绪数据

EmoKit判断情绪的数据大致分为两类：

* 第一类是人的主观意识可以控制，也就是可以伪装和掩饰的，比如语音、表情等；
* 另一类是普通人的主观意识不能控制的，比如心率等。我们采集人们情绪数据的方式也是多种多样的，比如通过app、穿戴设备、智能家居、车联网、机器人等。

####EmoKit情绪识别的准确率

* 情绪识别：在14年年初，EmoKit情绪识别的精度就超过了80%，也超过了国际的同行。

* 音乐情绪属性识别：EmoKit采用类似算法分析音乐的情绪属性，然后请作曲老师、音乐学院老师抽样评估，精度在80%以上。

  另外，每个用户也可以利用app海妖音乐自己评估

#### Emokit的优点

* 不仅能够识别情绪问题，还能解决情绪问题，帮助用户优化情绪，这样在用户看来形成了功能的闭环
* 算法是向全球开发者免费开放的





##SDK开发说明

###Android版本SDK开发说明

####一.主要功能

* SDK初始化  ```SDKAppInit```
* 脸部扫描识别情绪  ```RateDetect```
* 表情扫描识别情绪 ```ExpressionDetect```
* 语音识别情绪 ```EmotionDetect```

####二.预备工作 

**1.导入 SDK  **

将开发工具包中libs目录下的```emokitsdk.jar```复制到Android工程的libs目录(如果工程 无libs目录,请自行创建)中

**2.添加权限 **
在工程 ```AndroidManifest.xml ```文件中添加如下权限 

``````xml
<!--开启摄像头-->
<uses-feature android:name="android.hardware.camera"/>
<uses-feature android:name="android.hardware.flash"/> 
<uses-permission android:name = "android.permission.CAMERA"/>
<uses-permission android:name = "android.permission.WAKE_LOCK"/>
<!--设置录音-->
<uses-permission android:name = "android.permission.RECORD_AUDIO"/>
<!--网络状态-->
<uses-permission android:name = "android.permission.INTERNET" />
<uses-permission android:name = "android.permission.ACCESS_NETWORK_STATE" />
<uses-permission android:name = "android.permission.ACCESS_WIFI_STATE" />
<uses-permission android:name = "android.permission.CHANGE_NETWORK_STATE" />
<uses-permission android:name = "android.permission.READ_PHONE_STATE" />
<!--sd卡获得写的权限-->
<uses-permission android:name = "android.permission.WRITE_EXTERNAL_STORAGE" />                                    
``````

**3.添加ADI和KEY** 

初始化时候需要配置从EmoKit 开发者中心(http://dev.emokit.com/)申请的AID和 KEY。在```AndroidManifest.xml```中配置如下: 

``````xml
<meta-data 
		android:name="EMOKIT_AID" android:value="100001" />
<meta-data
		android:name="EMOKIT_KEY"
    android:value="98cd22f6f90141f8f1876dd2f5a27ea5" />
<meta-data 
    android:name="EMOKIT_RecordTaskAnimation" 
    android:value="1" />
``````

```EMOKIT_RecordTaskAnimation```为调用语音按钮时候是否启动交互框,默认为1启动;0为不启动 

**4.添加Activity **

``````xml
<activity 
		android:name="com.emokit.sdk.heartrate.FacedetectActivity"
    android:screenOrientation="portrait" >
</activity> 
<activity
		android:name="com.emokit.sdk.senseface.CameraActivity"
		android:screenOrientation="portrait" > 
</activity>
``````

**5.初始化SDK** 

* 添加 SDK 的初始化代码 

  在应用入口处Activity的onCreate方法内调用```SDKAppInit.createInstance(this)```; 初始化 SDK,示例代码如下: 

  ``````java
  @Override
  protected void onCreate(Bundle savedInstanceState){
  		super.on Create(savedInstanceState)
      SDKAppInit.createInstance(this)
  }
  ``````

* 开启 Debug 模式

  集成调试过程中若需查看 log 日志,请在应用入口处 Activity 的 onCreate 方法内调用 ```SDKAppInit.setDebugMode(true)```,否则默认为 false 。 

####三.语音识别情绪 

调用该方法后,语音识别在后台运行,分析和采集语音产生情绪识别结果。 

**1.监听器初始化 **

``````java
EmotionVoiceListener mRecognizerListener=new EmotionVoiceListener(){
	@Override
	public void onVolumeChanged(int volume){
			//实时分贝
	}

  @Override
  public woid onBeginOfSpeech(){
			//开始说话
  }

  @Override
  public void onEndOfSpeech(){
    	//结束说话
  }

	@Ovcrride
  public void onVoiceResult(String result){
    	//返回情绪结果
  }
}
``````

**2.启动语音分析 **

通过下面的代码启动语音情绪识别: 

``````java
EmotionDetect mEmotionDetect = EmotionDetect.createRecognizer(context, mInitListener);
		//初始化用户信息
		private InitListener mInitListener = new InitListener() {
		
    		@Override
				public void onInit(int code) {
						//注册用户信息: platflag应用名; userName用户名或设备ID;
						//password用户登录密码(可为空)
						SDKAppInit.registerforuid(platflag, userName, password); 
				}
};

//启动监听
mEmotionDetect.startListening(mRecognizerListener);
//停止监听
mEmotionDetect.stopListening(;
``````

**3.语音分析以及结果返回 **

* 结果返回: 

  - 成功结果

    ```json
    {"resultcode":"200","rc_main":"YC+","rc_main_value":"5.8","servertime":"20151030145217"}&&
    ```

    多情绪结果用&&分割

  - 错误结果

    ```json
    {"resultcode":"10000","reason":"传入的参数不正确","servertime":"20151030145703"}&&
    ```

当```resultcode```=20010时（网络错误），```reason```为采集的语音数据，有网时可再次发送请求分析情绪
当 ```resultcode```等于其他值时，```reason```为错误描述

``````java
mEmotionDetect.reAnalysisVoice(reason); //返回情绪结果同上
``````

**4.语音识别结果字段说明**

返回结果: 返回的字段格式为JSON格式的字符串 

* ```resultcode``` 结果码  
* ```rc_main``` 主要情绪
* ```rc_main_value``` 主要情绪分值
* ```servertime``` 服务器时间
* ```reason``` 错误描述或采集的语音数据 

#### 四.语音识别情绪和语义识别

调用该方法后，语音识别在后台运行，分析和采集语音产生情绪识别结果和语义结果， 请参照Demo，情绪结果和语义结果是异步返回的。 

工程导入```emokitsdk.jar```，```Msc.jar```， ```libmsc.so ```

**1.监听器初始化** 

``````java
/**
*语音识别监听器。
*/
		private SpeechEmotionListener mSpeechEmotionListener = new SpeechEmotionListener(){

    		@Override
				public void onVolumeChanged(int volume) {
						Log.e("tag", volume + "); 
				}

      	@Override
				public void onEndOfSpeech() {
						Log.e(" EmotionVoiceListener", "结束说话");
        }

      	@Override
				public void onBeginOfSpeech(){
						Log.e(" EmotionVoiceListener", "开始说话");
        }
      
				@Override
				public void onEmotionResult(String result) {
						//情绪结果
        }

        @Override
        public void onSpeechResult(String result) {
            //语义结果
        }
    };
``````

**2.启动语音语义分析 **

``````java
		SpeechEmotionDetect speechEmotionDetect = SpeechEmotionDetect.createRecognizer(this, mInitListener);
		speechEmotionDetect.startListening(mSpeechEmotionListener, SDKConstant.RC_TYPE_5,
false, "52c8cef6");
``````

**3.语音分析以及结果返回 **

语义结果为文字 

####五.脸部扫描识别情绪 

通过摄像头分析人脸采集心率，产生情绪结果 

**1.监听器初始化 **

``````java
EmoRateListener mEmoRateListener = new EmoRateListener () {
		@Override
		public void beginDetect() {
				//开始监测
		}

  	@Override
		public void endDetect(tring result) {
				//结束监测，返回情绪结果
    }
  
		@Override
		public void monitor(double rgbRed) {
				//实时红光色值变换，可用作显示心率波形
    }
};
``````

**2.启动心率采集 **

``````java
RateDetect mRateDetect = RateDetect.createRecognizer(context, mInitListener);
		//初始化用户信息
		private InitListener mInitListener = new InitListener() {
				@Override
				public void onInit(int code) {
						//注册用户信息: platflag应用名; userName用户名或设备ID; 
						// password用户登录密码(可为空)
						SDKAppInit.registerforuid(platflag, userName, password);
        }
    };

//设置摄像头参数
mRateDetect.setParameter(SDKConstant.FACING, SDKConstant.CAMERA_FACING_FRONT); 
//开始监听
mRateDetect.startRateListening(mEmoRateListener);
``````

**3.心率分析以及情绪结果返回**

- 结果返回: 

  - 成功结果

    ```json
    {"resultcode":"200","rc_main":"YC+","rc_main_value":"5.8","servertime":"20151030145217"}
    ```

  - 错误结果

    ```json
    {"resultcode":"10000","reason":"传入的参数不正确","servertime":"20151030145703"}
    ```

**4.心率识别结果字段说明 **

返回结果: 返回的字段格式为JSON格式的字符串 

* ```resultcode``` 结果码  
* ```rc_main``` 主要情绪
* ```rc_main_value``` 主要情绪分值
* ```servertime``` 服务器时间
* ```reason``` 错误描述 

####六.表情扫描识别情绪 

通过摄像头拍照，产生情绪结果 

**1.监听器初始化 **

``````java
ExpressionListener mExpressionListener =new ExpressionListener() {
		@Override
		public void beginDetect() {
				//开始监测
		}
		
  	@Override
		public void endDetect(String result) {
				//结束监测，返回情绪结果
		}
};
``````

**2.启动表情数据采集 **

``````java
ExpressionDetect mExpressionDetect = ExpressionDetect.createRecognizer(context, mInitListener);
		//初始化用户信息
		private InitListener mInitListener = new InitListener( {
				@Override
				public void onInit(int code) {
						//注册用户信息: platflag应用名; userName用户名或设备ID;
						// password用户登录密码(可为空)
						SDKAppInit.registerforuid(platflag,userName,password); 
				}
    }
                                                          
//设置摄像头参数
mExpressionDetect.setParameter(SDKConstant.FACING,SDKConstant.CAMERA_FACING_FRONT);
//开始监听
mExpressionDetect,startRateListening(mExpressionListener);
``````

**3.表情分析以及情绪结果返回**

* 脸部识别: 

  弹出拍照页面，将脸部对准拍照的小框，点击拍照，将拍摄出的脸部照片上传到服务器端。

* 结果返回: 

  * 成功结果

    ```json
    {"resultcode":"200","rc_main":"K","rc_main_value":"5.8","servertime":"20151030145217"}
    ```

  * 错误结果

    ``````json
    {"resultcode":"10000","reason":"传入的参数不正确","servertime":"20151030145703"}
    ``````

**4.表情识别结果字段说明 **

返回结果: 

返回的字段格式为JSON格式的字符串 

* ```resultcode``` 结果码 
* ```rc_main``` 主要情绪
* ```rc_main_value``` 主要情绪分值
* ```servertime``` 服务器时间
* ``` reason``` 错误描述 

####七.笔迹识别情绪 

通过写字的压感和速度来分析情绪 

**1.监听器初始化 **

``````java
HandWritingListener mHandWritingListener =new HandWritingListener() {
		@Override
		public void beginDetect() {
				//开始监测
		}
		
  	@Override
		public void endDetect(String result) {
				//结束监测，返回情绪结果
		}

  	@Override
		public void onPressureChanged(float pressure) {
    		//返回实时压力
		}
  
		@Override
		public void onSpeedChanged(float speed) {
				//返回实时速度
		}
};  
``````

**2.启动笔迹数据采集** 

``````java
HandWritingDetect mHandWritingDetect = HandWritingDetect.createRecognizer(context, mInitListener);
		//初始化用户信息
		private InitListener mInitListener = new InitListener(){
  			@Override
				public void onInit(int code) {
						//注册用户信息：platflag 应用名；userName 用户名或设备ID；
          	//password 用户登录密码（可为空）
          	SDKAppInit.registerforuid(platflag,userName,password); 
        }
    }

//准备开始监听
mHandWritingDetect.prepareDetect(mHandWritingListener,SDKConstant.RC_TYPE_5);

//在画板onTouchEvent事件中加入采集
mHandWritingDetect.collectHandwriting(event);
``````

**3.笔迹分析以及情绪结果返回 **

``````java
//结束采集，情绪结果通过监听mHandWritingListener返回
mHandWritingDetect.endDetect();
``````

* 结果返回: 

  * 成功结果

    ``````json
    {"resultcode":"200","rc_main":"K","rc_main_value":"5.8","servertime":"20151030145217"}
    ``````

  * 错误结果

    ``````json
    {"resultcode":"10000","reason":"传入的参数不正确","servertime":"20151030145703"}
    ``````

**4.笔迹识别结果字段说明 **

返回结果: 

返回的字段格式为JSON格式的字符串 

* ```resultcode```  结果码
* ```rc_main```  主要情绪
* ```rc_main_value```  主要情绪分值
* ```servertime```  服务器时间
* ```reason```  错误描述

####八.手指采集心率识别情绪 

通过手指采集心率识别情绪 

**1.监听器初始化**

``````java
EmoRateListener mEmoRateListener = new EmoRateListener(){
		@Override
  	public void beginDetect(){
    		//开始监测
  	}

		@Override
  	public void endDetect(String result) {
			//结束监测，返回情绪结果
		}
  
		@Override
		public void monitor(double rgbRed) {
				//实时红光色值变换，可用作显示心率波形
    }
  
		@Override
		public void onHeartRateValue (int value) {
				//返回实时心率值
		}
};
``````

**2.启动手指心率数据采集**

新建```Activity```继承```HeartRateMonitor```
创建自定义```layout```，```layout```中要含有```SurfaceView```
在```onCreate中```调用```intView(mSurfaceView,mEmoRateListener);```

**3.手指心率分析以及情绪结果返回**

``````java
//结束采集，情绪结果通过监听mEmoRateListener返回
mEmoRateListener.endDetect();
``````

* 结果返回：

  * 成功结果：

    ``````json
    {"resultcode":"200","rc_main":"K","rc_main_value":"5.8","servertime":"20151030145217"}
    ``````

  * 错误结果：

    ``````json
    {"resultcode":"10000","reason":"传入的参数不正确","servertime":"20151030145703"}
    ``````

**4.手指心率识别结果字段说明**

返回结果: 

返回的字段格式为JSON格式的字符串 

- ```resultcode``` 结果码 
- ```rc_main``` 主要情绪
- ```rc_main_value``` 主要情绪分值
- ```servertime``` 服务器时间
- ``` reason``` 错误描述 

​						 

####九.附录 

错误码列表 

| 错误值 | 含义         |
| ------ | ------------ |
| 10001  | 应用ID错误   |
| 10002  | 签名错误     |
| 10003  | 内部错误     |
| 10004  | 内部错误     |
| 10005  | 内部错误     |
| 10006  | 版本错误     |
| 10099  | 表情识别错误 |
| 20010  | 网络错误     |



###iOS版本SDK开发说明

####一.主要功能

* SDK初始化  ```EmoKitManager```
* 脸部扫描识别情绪  ```EMKEmoRate```
* 表情扫描识别情绪  ```EMKEmoFaceCamera```
* 语音识别情绪 ```EMKEmoVoice```

####二.预备工作

**1.导入 SDK**

添加 lib 文件夹(包含静态类库和头文件)

若是在 ios9 SDK 下编译，需在 plist 文件添加配置

**2.添加系统库 **

注册模块

``````swift
#import <SystemConfiguration/SystemConfiguration.h> 
``````

心率模块

``````swift
#import <AVFoundation/AVCaptureSession.h> 
#import <CoreMedia/CMSampleBuffer.h> 
``````

语音模块

``````swift
#import <AudioToolbox/AudioToolbox.h> #import <Accelerate/Accelerate.h> 
``````

**3.初始化 **

初始化时候需要配置从开发者中心(http://dev.emokit.com/)申请的 AID 和 KEY

* 在 AppDelegate.h 中配置如下: 

  ``````swift
  [EmoKitManager startAppKey:@"申请的key" AppId:@"申请的aid"];
  ``````

####三.语音识别情绪

语音识别通过采集和分析外界生意产生情绪结果

**1.监听器初始化**

``````swift
EMKEmoVoice* voiceView =[[ EMKEmoVoice alloc] init]; 
voiceView.delegate =self;
``````

**2.启动和停止语音分析**

``````swift
通过下面的代码启动语音情绪识别: 
[voiceView start]; 

通过下面的代码停止语音情绪识别: 
[voiceView stop]; 
``````

**3.语音分析结果返回**

``````swift
调用 EMKEmoVoiceDelegate 的

-(void)resposeVoiceResult:(NSArray*)resultArr
``````

**4.语音识别的其他属性配置**

``````swift
/** 
		是否正在检测
*/ 

@property(nonatomic, readonly, getter=isChecking)BOOL checking; 
/** 
不设置默认为7种情绪 

rc_type=1,返回24种情绪 
rc_type=27,返回7种情绪 
rc_type=35,返回5种情绪 
*/ 

@property (nonatomic, strong)NSString *rc_type; 
``````

语音识别返回的字段格式为 JSON 格式的字符串

* ```resultcode``` 结果码
* ```reason``` 结果描述
* ```rc_main``` 主要情绪
* ```rc_main_value``` 主要情绪分值

####四.脸部扫描识别情绪 

通过摄像头分析人脸采集心率，产生情绪标识结果 

**1.监听初始化 **

``````swift
EMKEmoRate *rateView=[[ EMKEmoRate alloc]initWithFrame: withVideoType:];
 [self.view addSubview: rateView];
 rateView.delegate =self; 
``````

**2.启动和停止心率采集 **

``````swift
/**
		开始心率检测
*/
-(void)start;
/**
		停止心率检测
*/
-(void)stop;
``````

**3.心率分析情绪结果返回 **

脸部识别 

检测前将眼睛对准红框，红框消失则开始分析 

分析完成后调用 ```EMKEmoRateDelegate``` 的 

``````swift
-(void)responseVideoResult:(NSDictionary*)dictionary; 
``````

心率识别返回的字段格式为 JSON 格式的字符串 :

* ```resultcode``` 结果码
* ```reason``` 结果描述
* ```rc_main``` 主要情绪 
* ```rc_main_value``` 主要情绪分值

**4.心率识别的其他属性配置 **

``````swift
/** 
		是否正在检测
*/ 

@property(nonatomic, readonly, getter=isChecking)BOOL checking; 

/** 
		不设置默认为7种情绪 
		rc_type=1,返回24种情绪 
		rc_type=2,返回7种情绪
		rc_type=3,返回5种情绪
*/ 
@property (nonatomic, strong)NSString *rc_type; 
``````

####五.表情扫描识别情绪 

通过摄像头拍照，产生情绪标识结果 

**1.监听器初始化 **

``````swift
EMKEmoFaceCamera *faceView = [[EMKEmoFaceCamera alloc]initWithVideoType:EMK_VideoTypeFont]; 

faceView.delegate =self; 
``````

**2.启动表情数据采集 **

``````swift
[ faceView start]; //开始采集 
``````

弹出拍照页面，将脸部对准拍照的小框，点击下方按钮进行拍照 

**3.表情分析情绪结果返回 **

分析完成后调用 ```EMKEmoFaceDelegate``` 的方法 

``````swift
-(void)responseFaceResult:(NSDictionary*)dictionary; 
``````

**4.表情识别的其他属性配置 **

``````swift
/** 
		拍照识别完成后界面是否自动消失，默认为YES 
*/ 

@property(nonatomic,assign)BOOL autoDisappear; 

/** 
		识别指定的脸部照片的情绪
*/ 
- (void)startWithPicture:(UIImage *)pic; 
``````

表情识别返回的字段格式为 JSON 格式的字符串 

``````json
{
		Image = "<UIImage: 0x14c703e70>, {684, 684}"; "rc_main" = K;
		"rc_main_value" = 99;
		resultcode = 0;
		setvertime = 20160422193405; 
} 
``````

* ```Image``` 识别情绪的照片
* ```rc_main``` 主要情绪
* ```rc_main_value``` 主要情绪分值
* ```resultcode``` 结果码 

####六.附录 

**1.错误码列表 **

| 错误值 | 含义             |
| ------ | ---------------- |
| 200    | 结果返回成功     |
| 10005  | 采集的数据不正确 |



###HTML5版本SDK开发说明

因为google chrome 浏览器升级，加强了对语音和拍照视频组件的安全性，导致过去的js文件加载问题。使用H5版本的SDK 需要以下步骤：

首先构建一个能访问https的web服务，然后将H5版本的js 文件导入。具体如下：

####一.语音情绪识别

#####1.1 语音脚本说明

访问 <https://api-web.emokit.com:1803/front/emokitsdk/record.html>将<https://api-web.emokit.com:1803/front/emokitsdk/js/recorderWorker.js>  <https://api-web.emokit.com:1803/front/emokitsdk/js/recorder.js>文件导入工程

仿照```record.html ```文件对如下参数修改

* ```audio ```: 音频对象

* ```callbackFun```: 自定义回调函数

* ```appid``` : SDK分配给开发者的应用ID,通过[www.emokit.com](http://www.emokit.com)网站注册后得到

* ```key``` : 开发者定义的密钥，通过[www.emokit.com](http://www.emokit.com/)网站注册后得到

* ```platid``` : 平台标识，开发者自己填写。

* ```uid``` : 终端用户的id。可以是终端用户的手机号或者设备id。

* **回调函数```callbackFun```**的返回参数为json格式

  失败返回格式：```{resultcode:”10000”,reason:”传入参数不正确”}```

  正确返回格式：```{resultcode:”200”,rc_main:”KA+”,rc_minor:”YL+”}```

#####1.2 代码示例

访问 <https://api-web.emokit.com:1803/front/emokitsdk/record.html>



####二.拍照情绪识别

#####2.1拍照脚本说明

<http://api-web.emokit.com:803/front/emokitsdk/jssdk/faceemo.js>或者<https://api-web.emokit.com:1803/front/emokitsdk/jssdk/faceemo.js>

重要函数说明:

* **```function picturedraw(callbackFun,appid,key,platid,uid)```** 是调用SDK程序进行图像分析的方法，该接口参数说明如下：
  * ```callbackFun```: 自定义回调函数
  * ```appid``` : SDK分配给开发者的应用ID,通过[www.emokit.com](http://www.emokit.com/)网站注册后得到
  * ```key``` : 开发者定义的密钥，通过[www.emokit.com](http://www.emokit.com/)网站注册后得到
  * ```platid``` : 平台标识，开发者自己填写。
  * ```uid``` : 终端用户的id。可以是终端用户的手机号或者设备id。

* **回调函数```callbackFun```**的返回参数为json格式

  失败返回格式：```{resultcode:”10000”,reason:”传入参数不正确”}```

  正确返回格式：```{resultcode:”200”,rc_main:”KA+”,rc_minor:”YL+”}```

#####2.2代码示例

https://api-web.emokit.com:1803/front/emokitdemo/faceemo.html



###微信版本SDK开发说明

####一.微信版本SDK脚本说明

引入SDK的js脚本，语音和图像都使用该脚本

* http://wechat.emokit.com/front/wxpz/wx.js

重要函数说明：

* **```function sendface(datas,call_back)```** 是调用SDK程序进行图像分析的方法，该接口参数说明如下：

  * ```datas```：开发者组织的数据，以json格式传输，类似的格式为

    ``````json
    var datas = {
         "uid" : open_id,
         "access_token" : access_token,
         "media_id" : serverId,
         "ghid" : appid,
         "emokit_appid" : emokit_appid,
         "emokit_key" : emokit_key
    };
    ``````

  * 以上列举参数说明：

    * ```uid```：终端用户者的openId 或者手机号码
    * ```access_token```：开发者微信访问的access_token
    * ```media_id```：上传到微信服务后得到的媒体id
    * ```ghid```：开发者应用Id
    * ```emokit_appid```：SDK分配给开发者的应用ID,通过[www.emokit.com](http://www.emokit.com/)网站注册后得到
    * ```emokit_key```：开发者定义的密钥，通过[www.emokit.com](http://www.emokit.com/)网站注册后得到
    * ```call_back```：为用户自定义的回调函数

* **回调函数```callbackFun```**的返回参数为json格式

  失败返回格式举例：```{resultcode:”10000”,reason:”传入参数不正确”}```

  正确返回格式举例：```{resultcode:”200”,rc_main:”KA+”,rc_minor:”YL+”}```

* **```function sendvoice(datas,call_back)```** 是调用SDK程序进行语音分析的接口，该接口参数说明如下：

  ```datas```和```call_back```参数说明同上

####二.语音情绪识别

基于微信提供的JS-SDK的音频接口进行开发，相关的音频接口请参考微信接口文档，程序中使用到了```startRecord```, ```stopRecord```, ```uploadVoice``` 三个微信接口

在调用```uploadVoice```接口成功后，组织数据调用SDK的语言分析接口```sendvoice```

代码示例：

``````html
<script src="http://libs.baidu.com/jquery/1.11.1/jquery.min.js"></script>
<script src="http://res.wx.qq.com/open/js/jweixin-1.0.0.js"></script>
<script src="http://wechat.emokit.com/front/wxpz/wx.js"></script>
<script type="text/javascript">
	var isRecord = true; // 是否开始录音
// 以下${}为freemarker中的标签，需要从action中传过来数据
	var appid = "${mapjson.appid}";
	var open_id = "${mapjson.open_id}";
	var jsapi_ticket = "${mapjson.jsapi_ticket}";
	var nonceStr = "${mapjson.nonceStr}";
	var timestamp = "${mapjson.timestamp}";
	var access_token = "${mapjson.access_token}";
	var ghid = appid;
	var emokit_appid = "100001";
	var emokit_key = "98cd22f6f90141f8f1876dd2f5a27ea5";
	wx.config({
		debug : false,
		appId : appid,
		timestamp : timestamp,
		nonceStr : nonceStr,
		signature : jsapi_ticket,
		jsApiList : [ 'startRecord', 'stopRecord', 'uploadVoice']
	});
	wx.ready(function() {
		$("#record").click(function() {
			console.log("is record=>" + isRecord);
			if (isRecord) {
				wx.startRecord();
				isRecord = false;
				$("#message").text("");
				$("#heartMsg").text("正在录音...");
			} else {
				wx.stopRecord({
					success : function(res) {
						var localId = res.localId;
						syncUploadVoice(localId);
					}
				});
				isRecord = true;
				$("#heartMsg").text("用心运算中,请稍等...");
			}
		})
	});
	// 异步调用sdk
	var syncUploadVoice = function(localIds) {
		console.log("the localId is" + localIds);
		var localId = localIds;
		function submitcallback() {
		}
		wx.uploadVoice({
			localId : localId, // 需要上传的音频的本地ID，由stopRecord接口获得
			isShowProgressTips : 1, // 默认为1，显示进度提示
			success : function(res) {
				var serverId = res.serverId; // 返回音频的服务器端ID
				var datas = {
					"uid" : open_id,
					"access_token" : access_token,
					"media_id" : serverId,
					"ghid" : appid,
					"emokit_appid" : emokit_appid,
					"emokit_key" : emokit_key
				};
				console.log("data us" + JSON.stringify(datas));
				sendvoice(datas, function(resinfo) {
					console.log("json call back" + JSON.stringify(resinfo));
					var resultcode = resinfo.resultcode;
					if ("10000" == resultcode) {
						$("#message").text("请再试一下,系统没忙过来...");
					} else if ("200" == resultcode) {
						if (undefined != resinfo.rc_main) {
							if (resinfo.rc_main.indexOf("+") != -1) {
								$("#message").text("您现在是正面情绪，请继续保持好心情!");
							} else {
								$("#message").text("您现在是负面情绪，需要改善一下心情哟!");
							}
						}
						console.log("rc_main:" + resinfo.rc_main + " rc_minor:" + resinfo.rc_minor);
					}
				});
			}
		});
	}
</script>
</html>
``````

####三.拍照情绪识别

基于微信提供的JS-SDK的音频接口进行开发，相关的音频接口请参考微信接口文档，程序中使用到了```chooseImage```, ```uploadImage``` 两个微信接口

在调用```uploadImage```接口成功后，组织数据调用SDK的语言分析接口```sendface```

代码分析：

``````html
<script src="http://libs.baidu.com/jquery/1.11.1/jquery.min.js"></script>
<script src="http://res.wx.qq.com/open/js/jweixin-1.0.0.js"></script>
<script src="http://wechat.emokit.com/front/wxpz/wx.js"></script>
<script type="text/javascript">
 	// 以下${}为freemarker中的标签，需要从action中传过来数据
	var appid = "${mapjson.appid}";
	var open_id = "${mapjson.open_id}";
	var jsapi_ticket = "${mapjson.jsapi_ticket}";
	var nonceStr = "${mapjson.nonceStr}";
	var timestamp = "${mapjson.timestamp}";
	var access_token = "${mapjson.access_token}";
	var ghid = appid;
	var emokit_appid = "100001";
	var emokit_key = "98cd22f6f90141f8f1876dd2f5a27ea5";
	wx.config({
		debug : false,
		appId : appid,
		timestamp : timestamp,
		nonceStr : nonceStr,
		signature : jsapi_ticket,
		jsApiList : [ 'chooseImage', 'uploadImage']
	});
	wx.ready(function() {
		$("#photo").click(function() {
			wx.chooseImage({
 				count: 1, // 默认9
				success : function(res) {
					var localId = res.localId;
					syncUploadImage(localId);
				}
			});
		})
	});
	// 异步调用sdk
	var syncUploadImage = function(localIds) {
		console.log("the localId is" + localIds);
		var localId = localIds;
		function submitcallback() {
		}
		wx.uploadImage({
			localId : localId, // 需要上传的图片的本地ID由chooseImage接口获得
			isShowProgressTips : 1, // 默认为1，显示进度提示
			success : function(res) {
				var serverId = res.serverId; // 返回图片下载后的本地ID
				var datas = {
					"uid" : open_id,
					"access_token" : access_token,
					"media_id" : serverId,
					"ghid" : appid,
					"emokit_appid" : emokit_appid,
					"emokit_key" : emokit_key
				};
				console.log("data us" + JSON.stringify(datas));
				sendface(datas, function(resinfo) { //调用SDK图像接口
					console.log("json call back" + JSON.stringify(resinfo));
					var resultcode = resinfo.resultcode;
					if ("10000" == resultcode) {
						$("#message").text("请再试一下,系统没忙过来...");
					} else if ("200" == resultcode) {
						if (undefined != resinfo.rc_main) {
							if (resinfo.rc_main.indexOf("+") != -1) {
								$("#message").text("您现在是正面情绪，请继续保持好心情!");
							} else {
								$("#message").text("您现在是负面情绪，需要改善一下心情哟!");
							}
						}
						console.log("rc_main:" + resinfo.rc_main + " rc_minor:" + resinfo.rc_minor);
					}
				});
			}
		});
	}
</script>
``````





###EmokitWearSDK

####1.导入SDK

创建一个AndoridWear工程，将```emokitsdk4.3.jar```（手机端引入）、```emokitwear.jar```（手机端、腕表端都需要引入）、```mobvoi-api.jar```（手机端、腕表端都需要引入）三个包引入到工程。

<http://www.emokit.com/>	下载```emokitsdk4.3.jar```

<http://developer.ticwear.com/>	下载```mobvoi-api.jar```

####2.添加权限

##### 1）手机端添加权限

``````java
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
<uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
<uses-permission android:name="android.permission.CHANGE_NETWORK_STATE" />
<uses-permission android:name="android.permission.READ_PHONE_STATE" />
``````

#####2）腕表端添加权限

``````java
<uses-permission android:name="android.permission.BODY_SENSORS" />
<uses-permission android:name="android.permission.WAKE_LOCK" />
<uses-permission android:name="android.permission.DEVICE_POWER" />
``````

####3.添加AID和KEY

初始化时候手机端需要配置从EmoKit 开发者中心(<http://dev.emokit.com/)申请的>AID和KEY。

```AndroidManifest.xml```中配置如下:

``````xml
<meta‐data
android:name="EMOKIT_AID"
android:value="XXXXXX"/>

<meta‐data
android:name="EMOKIT_KEY"
android:value="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"/>
``````

####4.初始化SDK

一定要在Application的```onCreate```中调用。

#####1）手机端初始化代码

``````java
MobileApiConfiguration configuration = new MobileApiConfiguration.Builder()
         .setPlatflag("EmokitWearSDK")//platflag 应用名
         .setUserName("userName")//userName 用户名或设备 ID
         .setPassword("10000")//password 用户登录密码(默认10000)
         .setRcType(rcType)//情绪结果种类，分为24种，7种，5种（见附录5）
         .create();
 EmokitApiManager.getInstance().mobileApiConfig(mContext,configuration);
``````

#####2）腕表端初始化代码

``````java
WearApiConfiguration configuration = new WearApiConfiguration.Builder()
 // 设置获取心率的超时时间,如果超过这个时间还没有接收到一个有用的心率值会自动停止获取心率
//获取心率期间最小时间10秒，输入参数小于10秒无效
.setHeartRateDuration(30*1000)
// 设置获取心率的时间，在这个规定时间内获取心率在成功获取第一个心率值开始倒计时
//获取心率超时时间最小20秒，输入参数小于20秒无效
.setHeartRateTimeOut(45 * 1000)

.create();
 EmokitApiManager.getInstance().wearApiConfig(getApplication(), configuration);
``````

####5.设置数据传输Service

#####1）手机端

手机端为了和腕表进行数据传递需要实现```MobileDataTransferService```并且在```AndroidManifest.xml```中注册

``````java
public class MobileEmokitService extends MobileDataTransferService{

private MobvoiApiClient mMobvoiApiClient;

@Override
protected void superMobvoiApiClient(MobvoiApiClient superMobvoiApiClient) {
//这个方法将父类的对象传递到子类中，子类可以根据这个对象进行数据的传递或者接收
		mMobvoiApiClient = superMobvoiApiClient;
}

@Override
public void onPeerConnected(Node arg0) {
		super.onPeerConnected(arg0);
}

@Override
public void onPeerDisconnected(Node arg0) {
		super.onPeerDisconnected(arg0);
}

@Override
public void onMessageReceived(MessageEvent messageEvent) {
		//必须调用
		super.onMessageReceived(messageEvent);
}

@Override
public void onDataChanged(DataEventBuffer eventBuffer) {
		//必须调用
		super.onDataChanged(eventBuffer);
		}
}
``````

#####2）腕表端

腕表端为了和手机进行数据传递需要实现```WearDataTransferService```并且在```AndroidManifest.xml```中注册

``````java
public class WearEmokitService extends WearDataTransferService {

private MobvoiApiClient mMobvoiApiClient;

 
@Override
protected void superMobvoiApiClient(MobvoiApiClient superMobvoiApiClient) {
		//这个方法将父类的对象传递到子类中，子类可以根据这个对象进行数据的传递或者接收
		 mMobvoiApiClient = superMobvoiApiClient;
}

@Override
public void onPeerConnected(Node arg0) {
		super.onPeerConnected(arg0);
}

@Override
public void onPeerDisconnected(Node arg0) {
		super.onPeerDisconnected(arg0);
}

@Override
public void onMessageReceived(MessageEvent messageEvent) {
		//必须调用
		super.onMessageReceived(messageEvent);
}

@Override
public void onDataChanged(DataEventBuffer eventBuffer) {
		//必须调用
		super.onDataChanged(eventBuffer);
		}
}
``````

#####3）AndroidManifest.xml中注册Service

手机端

`````xml
<service
		android:name=".emo.MobileEmokitService"
		android:enabled="true"
		android:exported="true">
		<intent-filter>
				<action android:name="com.mobvoi.android.wearable.BIND_LISTENER" />
		</intent-filter>
</service>
`````

 腕表端

``````xml
<service
		android:name=".emo.WearEmokitService"
		android:enabled="true"
		android:exported="true">
		<intent-filter>
				<action android:name="com.mobvoi.android.wearable.BIND_LISTENER" />
		</intent-filter>
</service>
``````

####6.注册广播监听

手机端和腕表端注册以下广播，主要是监听和回调方法，例如：开始测试回调，停止测试回调，返回情绪回调等。

#####1）手机端

Action为

动态注册：

```MobileWearableReceive.ACTION_MOBILE_EMO```

静态注册：

``````java
<action android:name="com.emokit.wear.action.MOBILE_EMO_LISTENER"/>

private MobileWearableReceive mMobileWearableReceive = new MobileWearableReceive() {
@Override

public void onStartHeartRateListener() {
		//开始测试心率
		Toast.makeText(mContext, "StartHeartRate", Toast.LENGTH_SHORT).show();
}

@Override
public void onCancelHeartRateListener() {
		//取消测试心率
		Toast.makeText(mContext, "CancelHeartRate", Toast.LENGTH_SHORT).show();
}

@Override
public void onArrayHeartRateListener(float[] heartRates) {
		//获取心率完成，收到心率数组
		Toast.makeText(mContext, "ArrayHeartRate", Toast.LENGTH_SHORT).show();
}

@Override
public void onEmotionListener(String emoJson) {
		//获取情绪结果
		Toast.makeText(mContext, "Emotion : " + emoJson, Toast.LENGTH_SHORT).show();
}

@Override
public void onErrorListener(String errCode) {
		//出错监听
		Toast.makeText(mContext, "errCode : " + errCode, Toast.LENGTH_SHORT).show();
		}
};
``````

#####2）腕表端

Action为

动态注册：

```WearWearableReceive.ACTION_WEAR_EMO```

静态注册：

``````java
<action android:name="com.emokit.wear.action.WEAR_EMO_LISTENER"/>


private WearWearableReceive mWearWearableReceive = new WearWearableReceive() {

@Override
public void onStartHeartRateListener() {
		//开始测试心率
		Toast.makeText(mContext, "StartHeartRate", Toast.LENGTH_SHORT).show();
		}

@Override
public void onCancelHeartRateListener() {
		//取消测试心率
		Toast.makeText(mContext, "CancelHeartRate", Toast.LENGTH_SHORT).show();
		}

@Override
public void onArrayHeartRateListener(float[] heartRates) {
		//获取心率完成，收到心率数组
		Toast.makeText(mContext, "ArrayHeartRate", Toast.LENGTH_SHORT).show();
		}

@Override
public void onHeartRateValueListener(int index, float value) {
		//每次获取的心率值
		//获取第index个心率
		//获取的心率值
		if(0 == index){
				Toast.makeText(mContext, "HeartRateValue : " + value + "   " + index, Toast.LENGTH_SHORT).show();
				}
		}

@Override
public void onEmotionListener(String emoJson) {
		//获取情绪结果
		Toast.makeText(mContext, "Emotion : " + emoJson, Toast.LENGTH_SHORT).show();
		}

@Override
public void onErrorListener(String errCode) {
		//出错监听
		Toast.makeText(mContext, "errCode : " + errCode, Toast.LENGTH_SHORT).show();
		}
};
``````

#####3）情绪结果

成功结果:

``````json
{"resultcode":"200","rc_main":"T","rc_main_value":"8.75","result_id":"14907293","exciting":"CH","exciting_trend":"UP","servertime":"20160319101255"}
``````

错误结果:

``````json
{"resultcode":"10000","reason":"传入的参数不正确","servertime":"20151030145703"}
``````

字段说明:

```resultcode``` 结果码

```rc_main``` 主要情绪

```rc_main_value``` 主要情绪分值

```result_id``` 返回情绪结果唯一id

```exciting``` 当前情绪状态

```exciting_trend``` 情绪走势

```servertime``` 服务器时间

```reason``` 错误描述

#####4）广播监听错误代码

手机端、腕表端```errCode```如下

``````java
public void onErrorListener(String errCode) {
		//出错监听
		}

/**获取情绪结果错误*/
PublicConstant.ERR_EMOTION_RESULT = "10000";

/**获取心率错误，没有获取到心率*/
PublicConstant.ERR_HEART_RATE = "10001";

/**
 *点击开始测试心率,手机腕表没有建立链接， 
 \* 1.手机端，没有链接到腕表
 \* 2.腕表端，没有链接到手机
 */

PublicConstant. ERR_CONNECT_START_HEART_RATE = "10002";

/**
 *停止测试心率,手机腕表没有建立链接 
 \* 1.手机端，没有链接到腕表(只有手机端，腕表端没链接到手机也可以取消)
 */

PublicConstant. ERR_CONNECT_STOP_HEART_RATE= "10003";

/**
 *手机端发送情绪结果,手机腕表没有建立链接 
 \* 1.没有链接到腕表
 */

PublicConstant.ERR_CONNECT _SEND_EMO_RESULT = "10004";

/**
 \* 手表端发送心率数组,手机腕表没有建立链接
 \* 1.没有链接到手机
 */

PublicConstant.ERR_CONNECT _SEND_HEART_RATE_ARRAY = "10005";
``````

####7.开始获取情绪和停止获取情绪

#####1）手机端

开始获取情绪

``````java
Intent intent = new Intent(mContext, MobileEmokitService.class);
intent.putExtra(PublicConstant.SERVICE_ACTION_START_HEART_RATE, "");
startService(intent);
``````

停止获取情绪

``````java
Intent intent = new Intent(mContext,MobileEmokitService.class);
intent.putExtra(PublicConstant.SERVICE_ACTION_STOP_HEART_RATE, "");
startService(intent);
``````

#####2）手表端

开始获取情绪

``````java
Intent intent = new Intent(MainActivity.this, WearEmokitService.class);
intent.putExtra(PublicConstant.SERVICE_ACTION_START_HEART_RATE, "");
startService(intent);
``````

停止获取情绪

``````java
Intent intent = new Intent(MainActivity.this, WearEmokitService.class);
intent.putExtra(PublicConstant.SERVICE_ACTION_STOP_HEART_RATE, "");
startService(intent);
``````

####8.附录

#####（1）结果码表

成功：```resultcode = 200```

错误:

| 错误值 | 含义         |
| ------ | ------------ |
| 10001  | 应用ID错误   |
| 10002  | 签名错误     |
| 10003  | 内部错误     |
| 10004  | 内部错误     |
| 10005  | 内部错误     |
| 10006  | 版本错误     |
| 10099  | 表情识别出错 |
| 20010  | 网络错误     |

#####（2）当前情绪状态

* LA:过于低迷

* LV:较为低迷

* CH:较为兴奋

* HO:过于兴奋

#####（3）情绪走势

* DN:走低 

* ST:维持 

* UP:走高

#####（4）情绪种类

返回情绪结果种类，分为24种，7种，5种

```MobileApiConfiguration.RC_TYPE_24```

```MobileApiConfiguration.RC_TYPE_7```

```MobileApiConfiguration.RC_TYPE_5```



###EmokitSDKMatch

####1.导入SDK

创建一个测试工程，将```emokitmatch.jar```、```jaudiotagger-2.2.5.jar```、```jl1.0.1.jar```添加到工程的libs下

#### 2.增加权限

``````java
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
<uses-permission android:name="android.permission.MOUNT_UNMOUNT_FILESYSTEMS" />
<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" />
``````

#### 3.初始化SDK

``````java
EmokitMatchApiConfiguration configuration = new EmokitMatchApiConfiguration.Builder()
		.setDeviceId(“XXXXXXXXXXXXXXXX”)//手机的设备唯一号
		//以下两个Aid和key是在http://www.emokit.com/网站上注册获取到的
		.setEmokitSDKAid("XXXXXX")
		.setEmokitSDKKey("XXXXXXXXXXXXXXXXXXXXXX")
		//情绪结果种类，分为24种，7种，5种（见附录1）
		.setRcType(EmokitMatchApiConfiguration.RC_TYPE_7)
		.create();
EmokitMatchApiManager.getInstance().initConfig(configuration);
``````

####4.根据情绪结果匹配内容

#####1）根据情绪匹配网络图片

``````java
EmokitMatchApiManager.getInstance().
//@param rcMain          当前情绪结果
//@param sex              性别0男性，1女性
//@param HttpHandler    处理网络请求的相应过程，网络请求为异步，但回调方法在UI
getImageFromNetwork("W",0,new HttpHandler() {...});
``````

####5.   网络访问监听

``````java
private HttpHandler httpHandler = new HttpHandler(){

@Override
protected void onFailure() {
		//UI线程中，网络请求失败
}

@Override
protected void onError() {
		//UI线程中，参数错误
}

@Override
protected void onSuccess(String result) {
		//UI线程中，网络请求成功
		//返回结果两种Json，音乐列表，图片列表
		}
};
``````

####6.根据情绪匹配结果

##### 1）图片列表

``````json
{
	"RESULT": {
			"icon": "http//:XXX.XXXX.com/ezlU87.jpg",   //对应情绪图片地址
			"story": "三国演义",                        //图片故事背景 
			"sid": "SG_001", 
			"icon_desc": "司马懿",                      //图片人物名字
			"emo_desc": "接纳；包容；吸收；柔顺",         //当前情绪描述
			"emo_sex": "0",                            //当前性别
			"icon_detail": "魏国大将，XXXX,并非胆怯。"    //图片人物描述
			}, 
		"STATUS": 0
}
``````

####7.附录

#####（1）情绪结果种类

返回情绪结果24种情绪：

```EmokitMatchApiConfiguration.RC_TYPE_24 ```

返回情绪结果7种情绪：

```EmokitMatchApiConfiguration.RC_TYPE_7 ```

返回情绪结果5种情绪：

```EmokitMatchApiConfiguration.RC_TYPE_5 ```





###语音情感识别说明

#### 一.AMR格式

amr语音文件上传接口说明

接口访问地址：<http://api-web.emokit.com:802/wechatemo/WxVoiceamr.do>  （正式） 

或者 http://api-web.emokit.com:803/wechatemo/WxVoiceamr.do（测试） 

输入参数：

* ```appid```  SDK分配给开发者的应用ID

* ```key```      开发者定义的密钥

* ```platid``` 平台标识，例如：HTML5标识为h5_tag

* ```uid```      开发者的名称

* ```type```  取值为3   代表返回5种情绪

此外还有amr文件

* 返回参数以json格式展现

  失败返回格式：

  ``````json
  {"infovoice":{"reason":"传入的参数不正确","resultcode":"10000","servertime":"20151106131334"},"status":"0"}
  ``````

  正确返回格式：

  ``````json
  {"infovoice":{"rc_main":"T","rc_main_value":"5","resultcode":"200","servertime":"20151107102545"},"status":"0"}
  ``````

示例程序：

``````xml
<form action="http://123.57.55.38:6080/wechatemo/WxVoiceamr.do" method="post" enctype="multipart/form-data">
		<input type="hidden" name="appid" value="100001"/>
		<input type="hidden" name="key" value="98cd22f6f90141f8f1876dd2f5a27ea5"/>
		<input type="hidden" name="platid" value="h5_tag"/>
		<input type="hidden" name="uid" value="dupf"/>
		<input type="file" name="file" />
		<input type="submit" name="submit">
</form>
``````



####二.WAV 格式

wav语音文件上传接口说明

接口访问地址：<http://api-web.emokit.com:802/wechatemo/ WxVoiceWAV.do>（正式）

或者 http://api-web.emokit.com:803/wechatemo/WxVoiceWAV.do（测试）

输入参数：

* ```appid```  SDK分配给开发者的应用ID

* ```key```      开发者定义的密钥

* ```platid``` 平台标识，例如：HTML5标识为h5_tag

* ```uid```      开发者的名称

* ```type```  取值为3   代表返回5种情绪，具体情绪码表参见说明

 此外还有wav文件

* 返回参数以json格式展现

  失败返回格式：

  ``````json
  {"infovoice":{"reason":"传入的参数不正确","resultcode":"10000","servertime":"20151106131334"},"status":"0"}
  ``````

  正确返回格式：

  ``````json
  {"infovoice":{"rc_main":"T","rc_main_value":"5","resultcode":"200","servertime":"20151107102545"},"status":"0"}
  ``````

示例程序：

``````xml
<form action="http://123.57.55.38:6080/wechatemo/WxVoiceWAV.do" method="post" enctype="multipart/form-data">
		<input type="hidden" name="appid" value="100001"/>
		<input type="hidden" name="key" value="98cd22f6f90141f8f1876dd2f5a27ea5"/>
		<input type="hidden" name="platid" value="h5_tag"/>
		<input type="hidden" name="uid" value="dupf"/>
		<input type="file" name="file" />
		<input type="submit" name="submit">
</form>
``````



## Emokit情绪描述

###Emokit五种情绪描述 

| 标签代码 | 情绪描述                 |
| -------- | ------------------------ |
| K        | 平静；放松；专注；出神； |
| C        | 伤感；郁闷；痛心；压抑； |
| Y        | 生气；失控；兴奋；宣泄； |
| M        | 开心；甜蜜；欢快；舒畅； |
| W        | 害怕；焦虑；紧张；激情； |



###Emokit七种情绪描述 

| 标签代码 | 情绪描述             | 英文     |
| -------- | -------------------- | -------- |
| K        | 平静;放松;专注;出神; | Calm     |
| D        | 忧愁;疑惑;迷茫;无助; | Confused |
| C        | 伤感;郁闷;痛心;压抑; | Sad      |
| Y        | 生气;蔑视;兴奋;失控; | Angry    |
| M        | 开心;甜蜜;欢快;舒畅; | Happy    |
| W        | 害怕;焦虑;紧张;激情; | Fear     |
| T        | 厌恶;反感;意外;惊讶; | Disgust  |



###Emokit24种情绪描述 

| 标签代码 | 正面情绪             | 英文                                                    |
| -------- | -------------------- | ------------------------------------------------------- |
| KA+      | 接纳;包容;吸收;柔顺; | accepting; embracing; absorbing;                        |
| KP+      | 专注;平静;出神;孤单; | Focused; peaceful; spellbound; lonely;                  |
| KR+      | 痛快;爽快;释放;放松; | piquant; straightforward; venting; relaxed;             |
| CT+      | 豪放;从容;开朗;豁达  | bold and unconstrained; calm; extroverted; open-minded; |
| CG+      | 决断;果敢;坚定;爽快; | resolute; bold; firm; willingly;                        |
| YC+      | 平和;美好;理智;祥和; | moderate; splendid; sane; harmonious;                   |
| YL+      | 舒适;轻松;自然;顺心; | comfortable; easy; natural; satisfactory;               |
| YV+      | 欢快;欢畅;舒畅;舒心; | cheerful; delightful; pleased; eased;                   |
| ML+      | 怜爱;同情;关心;甜蜜; | affectionate; sympathetic; caring; sweet;               |
| MS+      | 喜欢;开心;高兴;心动; | fond; happy; glad; touched;                             |
| WS+      | 积极;阳光;高涨;激情; | motivated; positive; upsurging; passionate;             |
| WC+      | 无畏;泰然;面对;激动; | fearless; poised; confronting; excited;                 |



| 标签代码 | 负面情绪             | 英文                                            |                      |
| -------- | -------------------- | ----------------------------------------------- | -------------------- |
| KA-      | 急躁;着急;憋躁;憋闷; | impatient; worried; restless; stifling;         | `躁狂症倾向`         |
| KP-      | 心乱;分心;空想;思念; | discomposed; distracted; airy-fairy; missed;    | `强迫症倾向`         |
| KR-      | 暴躁;烦躁;憋火;悸动; | irritable; hot-tempered; holding anger;         | `焦虑症倾向`         |
| CT-      | 伤感;哭泣;痛心;低落; | sentimental; crying; heartbroken; down;         | `抑郁症倾向`         |
| CG-      | 怯懦;犹豫;纠结;郁闷; | cowardly; hesitating; depressed;                | `强迫症倾向`         |
| YC-      | 生气;指责;攻击;冲动; | angry; accusatory; offensive; excited;          | `敌对症倾向`         |
| YL-      | 紧张;失调;失控;宣泄; | nervous; disordered; uncontroled; wreaking;     | `人际关系敏感症倾向` |
| YV-      | 压抑;窝心;别扭;想念; | repressed; annoyed; awkward; missed;            | `抑郁症倾向`         |
| ML-      | 哀伤;失落;幽怨;寂寞; | grieved; frustrated; hidden bitterness; lonely; | `偏执症倾向`         |
| MS-      | 记恨;怨恨;仇恨;哀怨; | grudge; resentful; hatred; plaintive;           | `偏执症倾向`         |
| WS-      | 消极;灰暗;低迷;颓废; | negative; dark; downturn; dispirited;           | `抑郁症倾向`         |
| WC-      | 恐惧;害怕;惊恐;焦虑; | afeared; scared; frightened; anxious;           | `恐怖症倾向`         |

