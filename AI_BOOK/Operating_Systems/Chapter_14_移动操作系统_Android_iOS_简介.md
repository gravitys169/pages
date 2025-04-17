# 第十四章：移动操作系统 (Android & iOS) 简介

移动操作系统是驱动智能手机、平板电脑等便携设备的核心软件。它们在设计上与桌面操作系统有显著不同，需要特别关注资源限制、用户交互、移动网络连接和安全性。本章将简要介绍两大主流移动操作系统——Android 和 iOS 的架构、关键特性以及它们面临的共同挑战。

## 14.1 移动操作系统的特点与挑战

移动操作系统在设计和实现上必须考虑以下关键因素：

-   **14.1.1 资源受限 (电池, CPU, 内存)**
    -   **电池续航:** 最重要的限制之一。操作系统必须采用积极的电源管理策略，如限制后台活动、合并网络请求、降低 CPU/GPU 频率、让设备快速进入睡眠状态等。
    -   **CPU 性能:** 相较于桌面 CPU，移动 CPU 性能（尤其持续性能）受功耗和散热限制。操作系统调度器需要平衡性能和功耗。异构多核 (big.LITTLE) 架构常见，需要调度器有效利用不同核心。
    -   **内存容量:** 移动设备内存通常比 PC 小且不可扩展。操作系统需要高效地管理内存，积极回收不活跃应用占用的内存，并可能采用内存压缩等技术。应用也需要优化内存使用。
    -   **存储空间:** 容量有限且速度可能不如桌面 SSD。操作系统和应用需要注意存储占用。
-   **14.1.2 用户体验与交互**
    -   **触摸优先:** 界面设计和交互模型围绕触摸屏进行优化。
    -   **即时响应:** 用户期望应用快速启动和流畅运行。UI 渲染必须在主线程高效完成，耗时操作需移至后台线程。
    -   **应用生命周期:** 应用可能随时被系统暂停或终止（例如，用户切换应用、内存不足）。操作系统定义了清晰的应用生命周期状态和回调，应用需要正确处理状态转换以保存数据和恢复状态。
    -   **通知系统:** 提供非侵入性的方式向用户传递信息。
    -   **传感器集成:** 需要方便地访问 GPS、加速度计、陀螺仪、摄像头等多种传感器。
-   **14.1.3 安全与隐私**
    -   **应用隔离:** 每个应用通常运行在独立的沙箱环境中，限制其访问系统资源和其他应用数据的能力。
    -   **权限模型:** 应用需要在使用敏感数据或功能（如位置、联系人、麦克风、摄像头）前获得用户明确授权。
    -   **代码签名与验证:** 确保应用来源可靠且未被篡改。应用商店扮演着重要的审核和分发角色。
    -   **数据加密:** 对用户数据进行加密存储是标准做法。
    -   **设备安全:** 提供锁屏、远程擦除、生物识别等功能。
-   **14.1.4 应用生态**
    -   **应用商店:** 是获取和分发应用的主要渠道，提供审核、支付、更新等机制。
    -   **开发框架与 API:** 提供丰富的 API 和工具包 (SDK) 供开发者构建应用。
    -   **向后兼容性:** 操作系统更新需要尽可能保持与旧应用的兼容性。

## 14.2 Android 操作系统

Android 是由 Google 主导开发的开源移动操作系统，基于 Linux 内核。它是目前全球市场份额最大的移动操作系统。

### 14.2.1 Android 架构

Android 采用分层架构：

```mermaid
graph TD
    A[应用程序 (Applications)]
    B[应用程序框架 (Java API Framework)]
    C[系统运行库 (Libraries & Android Runtime)]
    D[硬件抽象层 (HAL)]
    E[Linux 内核 (Linux Kernel)]

    A --> B;
    B --> C;
    C --> D;
    C --> E;
    D --> E;
    E --> F[硬件 (Hardware)];

    subgraph B
        ActivityManager[Activity Manager]
        WindowManager[Window Manager]
        ContentProviders[Content Providers]
        ViewSystem[View System]
        PackageManager[Package Manager]
        TelephonyManager[Telephony Manager]
        ResourceManager[Resource Manager]
        LocationManager[Location Manager]
        NotificationManager[Notification Manager]
        ...
    end

    subgraph C
        subgraph NativeLibs [原生 C/C++ 库]
            LibC[libc (Bionic)]
            MediaFramework[Media Framework]
            SurfaceManager[Surface Manager]
            LibWebCore[LibWebCore (WebKit/Blink)]
            SQLite[SQLite]
            OpenGL_ES[OpenGL/ES]
            Vulkan[Vulkan]
            ...
        end
        subgraph Runtime [Android Runtime (ART)]
            CoreLibs[核心 Java 库]
            ART_VM[ART 虚拟机]
        end
    end

    subgraph E
        DisplayDriver[Display Driver]
        CameraDriver[Camera Driver]
        BluetoothDriver[Bluetooth Driver]
        WiFiDriver[WiFi Driver]
        AudioDriver[Audio Driver]
        PowerManagement[Power Management (Binder IPC)]
        Binder[Binder IPC Driver]
        ...
    end

    style E fill:#f9f,stroke:#333,stroke-width:2px
    style D fill:#ccf,stroke:#333
    style C fill:#cfc,stroke:#333
    style B fill:#ffc,stroke:#333
```

-   **应用程序层 (Applications):** 用户直接交互的应用，如电话、短信、浏览器、地图以及第三方应用。这些应用通常使用 Java 或 Kotlin 语言编写。
-   **应用程序框架层 (Java API Framework):** 为应用开发者提供构建应用所需的各种 API。这些 API 由一系列管理器和服务组成，如活动管理器 (管理应用生命周期)、窗口管理器、内容提供器 (共享数据)、视图系统 (构建 UI)、包管理器 (管理应用安装)、通知管理器等。
-   **系统运行库层 (Libraries & Android Runtime):**
    -   **原生 C/C++ 库 (Native Libraries):** 提供核心功能支持，供框架层和应用调用。包括 Bionic C 库 (专为 Android 定制的 libc)、媒体框架、图形渲染库 (Surface Manager, OpenGL ES, Vulkan)、数据库引擎 (SQLite)、浏览器引擎 (WebKit/Blink) 等。
    -   **Android Runtime (ART):** Android 应用的主要运行环境。替代了早期的 Dalvik 虚拟机。
        -   **核心 Java 库:** 提供 Java 语言标准库和 Android 特定的核心功能。
        -   **ART 虚拟机:** 负责执行应用的字节码 (DEX 格式)。ART 主要采用**预编译 (Ahead-of-Time, AOT)** 策略，在应用安装时或设备空闲时将 DEX 字节码编译成本地机器码，提高了应用启动速度和运行效率。它也支持**即时编译 (Just-in-Time, JIT)** 和解释执行作为补充。ART 还负责内存管理 (垃圾回收) 和调试支持。
-   **硬件抽象层 (HAL - Hardware Abstraction Layer):** 提供了一个标准的接口，使得上层的 Java API 框架可以与底层的硬件驱动进行交互，而无需关心具体的硬件实现。例如，相机 HAL 定义了一套标准的相机操作接口，设备制造商需要提供实现该接口的库，供相机服务调用。这使得 Android 更容易适配不同的硬件。HAL 模块通常运行在用户空间。
-   **Linux 内核层 (Linux Kernel):** Android 基于定制的 Linux 内核。内核负责底层的系统管理，如进程管理、内存管理、设备驱动（显示、音频、相机、WiFi、蓝牙等）、电源管理、安全特性等。Android 对 Linux 内核进行了修改和增强，最重要的是引入了 **Binder IPC 机制**。

### 14.2.2 ART (Android Runtime) 与 Dalvik VM

-   **Dalvik VM (已弃用):** Android 早期的运行时环境。主要使用**即时编译 (JIT)**，在应用运行时将 DEX 字节码编译成本地代码。垃圾回收器效率相对较低。
-   **ART (Android Runtime):**
    -   **预编译 (AOT):** 主要优势。在安装或空闲时编译，减少运行时开销，启动更快，更省电。生成的本地代码直接执行。
    -   **改进的垃圾回收 (GC):** 更高效、更低暂停时间的 GC 算法。
    -   **更好的调试支持。**
    -   **DEX 格式:** 两者都执行 DEX (Dalvik Executable) 字节码，这是一种针对移动设备优化的紧凑格式。Java/Kotlin 源码先编译成 Java 字节码 (.class)，再通过 `dx` 或 `d8` 工具转换为 DEX 字节码 (.dex)。

### 14.2.3 Activity Manager 与应用生命周期

-   **Activity Manager:** Android 框架层的核心服务之一，负责管理四大应用组件（Activity, Service, Broadcast Receiver, Content Provider）的生命周期，特别是 Activity（代表应用的单个屏幕/UI 界面）。
-   **应用生命周期:** 为了管理内存和响应用户操作，Android 定义了严格的 Activity 生命周期状态和回调方法：
    -   `onCreate()`: Activity 创建时调用，进行初始化。
    -   `onStart()`: Activity 变为可见。
    -   `onResume()`: Activity 到达前台，可以与用户交互。
    -   `onPause()`: Activity 被部分遮挡或即将进入后台，应停止动画、保存数据。
    -   `onStop()`: Activity 完全不可见。
    -   `onDestroy()`: Activity 被销毁前调用，释放资源。
    -   `onRestart()`: Activity 从停止状态重新启动时调用。
-   **进程生命周期:** Android 根据应用组件的状态和重要性将进程分为不同级别（如前台进程、可见进程、服务进程、缓存进程）。当内存不足时，系统会按照优先级从低到高（缓存 -> 服务 -> 可见 -> 前台）终止进程以回收内存。应用需要能在其 Activity 或 Service 被销毁后正确恢复状态。

### 14.2.4 Binder IPC 机制

-   **背景:** Android 系统中有大量的进程（应用进程、系统服务进程）需要相互通信。传统的 Linux IPC 机制（如管道、套接字）对于移动设备来说开销较大或不够灵活。
-   **Binder:** Android 基于 OpenBinder 开发的一套高效、安全的**远程过程调用 (RPC)** 机制，是 Android 系统服务和应用间通信的基础。
    -   **架构:** 基于 C/S 模型。系统服务作为 Server 提供接口，应用作为 Client 调用接口。
    -   **驱动:** 内核包含一个特殊的 Binder 驱动 (`binder.ko`)，负责进程间的数据传输和权限控制。
    -   **接口描述语言 (AIDL - Android Interface Definition Language):** 用于定义服务接口，工具会自动生成 Client (Proxy) 和 Server (Stub) 端的 Binder 通信代码。
    -   **数据传输:** Binder 允许传输基本数据类型、实现了 Parcelable 接口的对象以及 Binder 对象本身（用于传递服务引用）。数据传输通常只需要一次内存拷贝（从发送方进程到内核，再从内核映射到接收方进程），效率较高。
    -   **线程管理:** 服务端通常维护一个 Binder 线程池来处理并发的客户端请求。
    -   **安全:** Binder 驱动会验证调用方的 UID/PID，允许服务根据调用者身份进行权限检查。
-   **应用:** 几乎所有的 Android 系统服务（Activity Manager, Package Manager, Window Manager 等）都通过 Binder 提供接口。应用间的通信（如通过 AIDL 实现跨进程服务调用）也使用 Binder。

### 14.2.5 电源管理

Android 采用多种策略来延长电池续航：

-   **Doze (打盹) 模式:** 当设备长时间静止、屏幕关闭且未充电时，系统会进入 Doze 模式，大幅限制应用的后台活动、网络访问和同步。系统会定期提供短暂的"维护窗口"允许应用执行延迟的任务。
-   **App Standby (应用待机):** 系统会识别用户长时间未使用的应用，并限制其后台网络访问和同步。
-   **后台限制:** 对应用的后台服务、广播接收器施加更严格的限制，防止应用在后台滥用资源。
-   **唤醒锁 (Wakelocks):** 允许应用阻止 CPU 或屏幕进入睡眠状态，但必须谨慎使用且及时释放。
-   **JobScheduler / WorkManager:** 推荐的 API，用于调度可延迟的后台任务（如下载、同步）。系统可以在合适的时机（如设备充电、连接 Wi-Fi）批量执行这些任务，减少唤醒次数。

### 14.2.6 安全模型

-   **应用沙箱:** 每个 Android 应用默认运行在自己的 Linux 用户 ID (UID) 下，拥有独立的进程和数据目录 (`/data/data/<package_name>`)。文件系统权限确保应用无法访问其他应用的数据。
-   **权限系统:**
    -   **安装时权限 (早期):** 应用在安装时声明所需权限，用户一次性授予。
    -   **运行时权限 (Android 6.0+):** 对于危险权限（如访问位置、相机、联系人），应用需要在运行时动态请求用户授权。用户可以随时在系统设置中管理应用权限。
-   **代码签名:** 所有 Android 应用都必须使用开发者的私钥进行签名。签名用于验证应用作者身份和确保应用更新来自同一作者，防止应用被篡改。
-   **Verified Boot (验证启动):** 确保设备启动加载的软件（从引导加载程序到系统分区）都来自可信来源且未被修改。
-   **SELinux (Security-Enhanced Linux):** 在 Android 中强制实施更细粒度的访问控制策略 (MAC - Mandatory Access Control)，限制系统进程和应用的权限，即使 root 用户也受其约束，提高了系统整体的安全性，减少了提权漏洞的影响。
-   **Google Play Protect:** Google Play 提供的安全服务，扫描应用是否存在恶意行为。

## 14.3 iOS 操作系统

iOS 是苹果公司为其 iPhone、iPad (iPadOS)、iPod Touch 开发的专有移动操作系统。它以流畅性、易用性、强大的生态系统和对安全隐私的关注而著称。

### 14.3.1 iOS 架构

iOS 的架构与 macOS 非常相似，共享 Darwin 核心和许多核心框架。

```mermaid
graph TD
    A[应用程序层 (Applications)]
    B[Cocoa Touch 层]
    C[媒体层 (Media Layer)]
    D[核心服务层 (Core Services Layer)]
    E[核心操作系统层 (Core OS Layer / Darwin)]

    A --> B;
    B --> C;
    B --> D;
    C --> D;
    C --> E;
    D --> E;
    E --> F[设备硬件 (Device Hardware)];

    subgraph B
        UIKit[UIKit (UI 框架)]
        MapKit[MapKit]
        PushKit[Push Notification]
        CallKit[CallKit]
        GameKit[GameKit]
        HealthKit[HealthKit]
        ...
    end

    subgraph C
        Graphics[Graphics (Core Graphics, Metal, OpenGL ES)]
        Audio[Audio (Core Audio, AVFoundation)]
        Video[Video (AVFoundation, Core Media)]
        AirPlay[AirPlay]
        ...
    end

    subgraph D
        CoreFoundation[Core Foundation]
        CFNetwork[CFNetwork]
        CoreLocation[Core Location]
        CoreMotion[Core Motion]
        Foundation[Foundation (Objective-C/Swift)]
        Security[Security Services (Keychain)]
        CoreData[Core Data]
        ...
    end

    subgraph E
        ExternalAccessory[External Accessory Framework]
        Accelerate[Accelerate Framework]
        System[System (libSystem)]
        XNU[XNU Kernel]
        Drivers[Device Drivers]
    end

    style E fill:#f9f,stroke:#333,stroke-width:2px
```

-   **应用程序层 (Applications):** 用户安装的 App Store 应用和系统自带应用。
-   **Cocoa Touch 层:** 提供构建 iOS 应用所需的主要框架。
    -   **UIKit:** iOS 应用的 UI 框架，提供窗口、视图、控件、触摸事件处理、应用生命周期管理 (UIApplication, AppDelegate, SceneDelegate) 等。对应 macOS 的 AppKit。
    -   其他高级框架如 MapKit, PushKit, CallKit, GameKit, HealthKit 等。
-   **媒体层 (Media Layer):** 提供图形、音频和视频技术。包括 Core Graphics (2D 绘图), Metal (高性能图形/计算), Core Audio (音频处理), AVFoundation (音视频播放录制) 等。
-   **核心服务层 (Core Services Layer):** 提供应用所需的基础系统服务，大部分不涉及 UI。包括 Core Foundation, Foundation (与 macOS 共享), Core Location (定位), Core Motion (运动传感器), Security (安全/钥匙串), Core Data (数据持久化) 等。
-   **核心操作系统层 (Core OS Layer / Darwin):** iOS 的底层基础，与 macOS 共享 Darwin 核心。
    -   **系统库 (libSystem):** 包含 POSIX API、线程、网络、文件 I/O 等底层接口。
    -   **框架:** 如 Accelerate (数值计算优化), External Accessory (与硬件配件通信)。
    -   **XNU 内核:** 负责进程/线程管理、内存管理、文件系统、网络、驱动程序 (通过 I/O Kit)。iOS 的 XNU 内核针对移动设备进行了优化（如电源管理）。

### 14.3.2 XNU 内核基础

iOS 使用与 macOS 相同的 XNU 混合内核（Mach + BSD + I/O Kit），但针对移动场景进行了大量优化：

-   **电源管理:** 更积极的休眠策略，对 CPU、GPU、无线电等组件的精细控制。
-   **内存管理:** 对内存更加敏感，系统会更积极地终止后台应用以回收内存（见下文）。
-   **实时性:** 对触摸响应、音频/视频处理等任务提供更好的实时性保障。
-   **安全性:** 内核层面的安全加固。

### 14.3.3 应用生命周期与沙箱

-   **应用生命周期:** iOS 应用的生命周期由 UIKit 框架管理 (`UIApplicationDelegate` / `UISceneDelegate`)。状态包括：
    -   Not Running: 应用未启动或已被终止。
    -   Inactive: 应用在前台但未接收事件（如来电时）。
    -   Active: 应用在前台且正在接收事件。
    -   Background: 应用在后台执行代码（时间有限）。
    -   Suspended: 应用驻留在内存中，但**不执行任何代码**。这是应用进入后台后的常见状态，以节省电量和 CPU。系统可以在内存不足时**无通知**地从 Suspended 状态终止应用。应用必须能在下次启动时恢复状态。
-   **后台执行:** iOS 对后台执行有严格限制。只有特定类型的应用（如音乐播放、VoIP、位置更新、后台下载）被允许长时间在后台运行，且需要声明后台模式并遵守规则。普通应用进入后台后只有很短的时间完成任务，然后会被挂起 (Suspended)。
-   **应用沙箱:** 每个 iOS 应用都运行在严格的沙箱中。每个应用都有自己的私有**容器目录 (Container Directory)**，只能读写自己容器内的文件。访问容器外的资源（如照片库、联系人、位置信息）需要通过系统提供的 API 并获得用户明确授权。这极大地限制了恶意应用或存在漏洞的应用可能造成的损害。

### 14.3.4 IPC 机制 (XPC)

-   **XPC Services:** iOS (和 macOS) 推荐的进程间通信 (IPC) 机制。它提供了一种安全、异步的方式来实现服务分解和权限分离。
    -   **目标:** 将应用程序的功能分解为更小的、独立的 XPC 服务进程，每个服务拥有尽可能少的权限。主应用通过 XPC 与这些服务通信。
    -   **优点:**
        -   **提高安全性:** 如果某个服务进程被攻破，由于其权限受限，损害范围较小。
        -   **提高稳定性:** 服务进程崩溃不会影响主应用程序。`launchd` 可以自动重启崩溃的服务。
        -   **提高响应性:** 将耗时任务移到 XPC 服务中，避免阻塞主线程。
    -   **机制:** 基于 Mach 端口，但提供了更高级的、面向对象的 API。使用接口协议 (Protocol) 定义服务接口，自动处理序列化和反序列化。通信是异步的。
-   **其他 IPC:** 底层的 Mach 端口通信仍然可用，但也存在 URL Scheme、UIActivityViewController (分享)、App Groups (在同一开发者的不同应用间共享数据) 等机制。

### 14.3.5 安全特性

iOS 以其强大的安全特性而闻名：

-   **硬件安全:**
    -   **Secure Enclave:** (A7 芯片及以后) 独立的安全协处理器，存储和处理 Touch ID/Face ID 数据、文件加密密钥 (Data Protection keys) 等，主 CPU 无法直接访问这些密钥。
    -   **启动链信任 (Secure Boot Chain):** 从硬件 Boot ROM 开始，每一级启动加载程序和操作系统内核都必须经过 Apple 的数字签名验证，确保系统软件未被篡改。
-   **系统安全:**
    -   **强制代码签名:** 所有在设备上运行的代码（应用、框架、系统组件）都必须经过 Apple 或注册开发者签名。不允许执行未签名或签名无效的代码（除非是越狱设备）。
    -   **沙箱 (App Sandbox):** 如前所述，严格限制应用访问范围。
    -   **地址空间布局随机化 (ASLR):** 内核、系统库、应用代码的加载地址随机化，增加内存攻击难度。
    -   **数据执行保护 (DEP):** 将内存区域标记为不可执行 (NX bit)，防止在数据区（如栈、堆）执行恶意代码。
    -   **指针认证码 (PAC - Apple Silicon):** 硬件级别的安全特性，用于验证函数指针和返回地址是否被篡改，防御面向返回编程 (ROP) 和面向跳转编程 (JOP) 攻击。
-   **数据安全:**
    -   **数据保护 (Data Protection):** 对闪存存储上的文件进行硬件加速加密 (AES-256)。文件根据其敏感度（由应用指定保护等级）使用不同的密钥加密。某些密钥（如需要设备解锁才能访问的文件）受到设备密码和 Secure Enclave 的保护。
    -   **钥匙串 (Keychain):** 安全存储密码、密钥、证书等，受硬件加密和设备密码保护。
-   **隐私保护:**
    -   **运行时权限:** 严格的权限模型 (TCC)，访问敏感数据（位置、联系人、照片、麦克风、摄像头、蓝牙等）需要用户授权。
    -   **限制广告跟踪 (IDFA):** 用户可以选择限制广告标识符的使用。
    -   **差分隐私 (Differential Privacy):** 在收集用户数据用于改进服务时（如输入法建议），加入噪音以保护个体用户隐私。

## 14.4 Android 与 iOS 的比较

| 特性             | Android                                      | iOS                                          |
| :--------------- | :------------------------------------------- | :------------------------------------------- |
| **核心**         | Linux 内核 (开源)                            | XNU 混合内核 (Darwin 开源基础, 上层闭源)       |
| **开发语言**     | Java, Kotlin (主要), C/C++ (NDK)             | Swift, Objective-C (主要)                      |
| **运行时**       | ART (AOT 编译 DEX 字节码)                     | 直接执行本地机器码 (编译时生成)                |
| **应用分发**     | Google Play (主要), 第三方商店, Sideloading | App Store (唯一官方渠道, 限制严格)           |
| **开放性**       | 更开放, 可定制性高                           | 更封闭, 软硬件高度集成                       |
| **文件系统**     | ext4, F2FS (常见), 其他 Linux 支持的文件系统  | APFS (现代), HFS+ (旧版)                     |
| **IPC**          | Binder (主要), Socket, Pipe                  | XPC (推荐), Mach Ports, URL Scheme             |
| **后台处理**     | 相对宽松 (受 Doze, Standby 限制)             | 非常严格 (大部分应用会被 Suspend)             |
| **沙箱**         | 基于 Linux UID/GID, SELinux 加固             | 非常严格的容器化沙箱                         |
| **代码执行**     | 允许 JIT, 解释执行                           | 强制代码签名, 通常不允许动态生成/修改代码执行 |
| **硬件抽象**     | HAL (标准化接口, 厂商实现)                 | 驱动程序与内核紧密集成 (I/O Kit)             |
| **碎片化**       | 严重 (多厂商, 多版本, 定制 UI)               | 基本无 (Apple 控制硬件和软件更新)            |
| **安全更新**     | 依赖厂商和运营商推送, 速度慢                 | Apple 直接推送, 速度快, 覆盖率高             |
| **默认浏览器引擎** | Blink (基于 WebKit)                          | WebKit                                       |

## 14.5 总结

Android 和 iOS 是当今移动世界的两大巨头，它们都基于成熟的操作系统内核（Linux 和 XNU），并针对移动设备的特殊需求（资源限制、触摸交互、安全隐私）进行了大量优化和创新。

-   **Android** 以其开源、开放和灵活性著称，拥有庞大的硬件生态系统和市场份额。其架构特点包括 Linux 内核、ART 运行时、Binder IPC 和 HAL。挑战主要在于碎片化和安全更新的延迟。
-   **iOS** 则以其软硬件高度集成、流畅的用户体验、强大的应用生态和领先的安全隐私保护而闻名。其架构与 macOS 一脉相承，特点包括 XNU 内核、直接执行本地代码、严格的沙箱和后台管理、XPC 以及多层硬件和软件安全机制。缺点是系统封闭，可定制性差。

两者在应用生命周期管理、电源优化、权限控制、安全沙箱等方面采用了相似的策略，但具体实现和侧重点有所不同。理解它们的核心架构和设计理念，对于移动应用开发者和系统研究者都至关重要。移动操作系统的竞争和发展，持续推动着整个计算技术的进步。 