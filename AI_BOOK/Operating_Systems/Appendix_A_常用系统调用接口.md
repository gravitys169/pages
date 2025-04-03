# 附录 A：常用系统调用接口 (POSIX, Win32)

本附录列出了 POSIX（Portable Operating System Interface）标准和 Windows API (Win32) 中一些最常用和基础的系统调用或API函数。理解这些接口有助于深入了解应用程序如何与操作系统内核交互以获取服务。

**注意：** 这并非详尽无遗的列表，仅选取了具有代表性的函数。具体的函数签名、参数和行为可能因操作系统版本和实现而异。

---

## POSIX 系统调用

POSIX 是 IEEE 为维护操作系统之间兼容性而制定的一系列标准。Linux、macOS、BSD 等众多类 Unix 系统都遵循或部分遵循 POSIX 标准。

### 1. 进程管理

| 系统调用       | 描述                                                     |
| -------------- | -------------------------------------------------------- |
| `fork()`       | 创建一个新进程（子进程），几乎是调用进程（父进程）的副本。   |
| `execve()`     | 在当前进程上下文中加载并运行一个新的程序，替换当前进程映像。   |
| `wait()`/`waitpid()` | 父进程等待其子进程状态改变（例如终止）。               |
| `exit()`       | 终止调用进程，并向父进程返回一个退出状态。               |
| `getpid()`     | 获取调用进程的进程 ID (PID)。                            |
| `getppid()`    | 获取调用进程的父进程 ID (PPID)。                         |
| `nice()`       | 修改进程的调度优先级。                                   |
| `kill()`       | 向指定进程或进程组发送一个信号。                         |
| `signal()`/`sigaction()` | 设置处理特定信号的方式（信号处理程序）。               |
| `sleep()`      | 使调用进程挂起指定的秒数。                               |

### 2. 文件系统操作

| 系统调用         | 描述                                                         |
| ---------------- | ------------------------------------------------------------ |
| `open()`         | 打开或创建一个文件，返回一个文件描述符。                       |
| `close()`        | 关闭一个打开的文件描述符。                                     |
| `read()`         | 从文件描述符读取数据到缓冲区。                                 |
| `write()`        | 将缓冲区的数据写入文件描述符。                                 |
| `lseek()`        | 改变文件描述符的读写偏移量。                                   |
| `stat()`/`fstat()`/`lstat()` | 获取文件的元数据（状态信息），如大小、权限、时间戳等。         |
| `mkdir()`        | 创建一个新目录。                                             |
| `rmdir()`        | 删除一个空目录。                                             |
| `link()`         | 创建一个指向现有文件的新硬链接。                               |
| `unlink()`       | 删除一个文件名（硬链接）。当链接计数为零且无进程打开该文件时，文件被删除。 |
| `symlink()`      | 创建一个符号链接（软链接）。                                   |
| `chmod()`/`fchmod()` | 更改文件的访问权限。                                         |
| `chown()`/`fchown()` | 更改文件的所有者和组。                                       |
| `mount()`        | 挂载一个文件系统。                                           |
| `umount()`       | 卸载一个文件系统。                                           |
| `pipe()`         | 创建一个匿名管道，用于进程间通信。                             |
| `dup()`/`dup2()`   | 复制一个文件描述符。                                         |
| `fcntl()`        | 对打开的文件描述符执行多种控制操作（如获取/设置文件状态标志、锁）。 |

### 3. 内存管理

| 系统调用   | 描述                                                               |
| ---------- | ------------------------------------------------------------------ |
| `brk()`/`sbrk()` | 改变数据段的大小（调整堆的末端）。通常由 `malloc()` 等库函数间接使用。 |
| `mmap()`   | 在调用进程的虚拟地址空间中创建新的内存映射（可以映射文件或匿名内存）。 |
| `munmap()` | 删除一个内存映射。                                                   |

### 4. 进程间通信 (IPC)

| 系统调用/机制 | 描述                                                               |
| ------------- | ------------------------------------------------------------------ |
| `pipe()`      | 创建匿名管道。                                                     |
| `mkfifo()`    | 创建命名管道 (FIFO)。                                               |
| 信号 (`kill()`, `signal()`, `sigaction()`) | 异步通知机制。                                                   |
| `shmget()`    | 创建或获取一个共享内存段标识符。                                     |
| `shmat()`     | 将共享内存段附加到调用进程的地址空间。                               |
| `shmdt()`     | 将共享内存段从调用进程的地址空间分离。                               |
| `shmctl()`    | 对共享内存段执行控制操作。                                         |
| `semget()`    | 创建或获取一个信号量集标识符。                                     |
| `semop()`     | 对信号量集执行原子操作 (P/V)。                                     |
| `semctl()`    | 对信号量集执行控制操作。                                         |
| `msgget()`    | 创建或获取一个消息队列标识符。                                     |
| `msgsnd()`    | 向消息队列发送一条消息。                                           |
| `msgrcv()`    | 从消息队列接收一条消息。                                           |
| `msgctl()`    | 对消息队列执行控制操作。                                         |
| `socket()`    | 创建一个通信端点 (socket)。                                        |
| `bind()`      | 将 socket 绑定到一个本地地址（IP 地址和端口号）。                     |
| `listen()`    | 将 socket 置于监听状态，等待传入连接。                               |
| `accept()`    | 接受一个传入的连接请求，创建一个新的已连接 socket。                    |
| `connect()`   | 主动发起一个连接到远程 socket。                                      |
| `send()`/`recv()` | 在已连接的 socket 上发送/接收数据。                                  |
| `sendto()`/`recvfrom()` | 在无连接的 socket (UDP) 上发送/接收数据。                            |

---

## Windows API (Win32)

Win32 API 是 Windows 操作系统的主要应用程序编程接口。它比 POSIX 更为庞大和复杂，提供了丰富的功能。

### 1. 进程与线程管理

| API 函数                     | 描述                                                               |
| ---------------------------- | ------------------------------------------------------------------ |
| `CreateProcess()`            | 创建一个新进程及其主线程。                                         |
| `ExitProcess()`              | 终止调用进程及其所有线程。                                         |
| `TerminateProcess()`         | 强制终止指定进程及其所有线程。                                     |
| `GetCurrentProcessId()`      | 获取调用进程的进程 ID。                                              |
| `OpenProcess()`              | 获取指定进程的句柄，以进行后续操作。                                 |
| `CreateThread()`             | 在调用进程中创建一个新线程。                                       |
| `ExitThread()`               | 终止调用线程。                                                     |
| `TerminateThread()`          | 强制终止指定线程。                                                 |
| `GetCurrentThreadId()`       | 获取调用线程的线程 ID。                                              |
| `SuspendThread()`/`ResumeThread()` | 挂起/恢复指定线程的执行。                                        |
| `WaitForSingleObject()`/`WaitForMultipleObjects()` | 等待一个或多个内核对象（如进程、线程、事件、互斥体）变为 signaled 状态。 |
| `Sleep()`                    | 使调用线程挂起指定的毫秒数。                                       |

### 2. 文件系统操作

| API 函数                | 描述                                                                 |
| ----------------------- | -------------------------------------------------------------------- |
| `CreateFile()`          | 创建或打开一个文件或 I/O 设备（如管道、控制台），返回一个句柄。          |
| `CloseHandle()`         | 关闭一个打开的对象句柄（包括文件句柄）。                               |
| `ReadFile()`/`ReadFileEx()` | 从文件句柄读取数据到缓冲区。                                         |
| `WriteFile()`/`WriteFileEx()` | 将缓冲区的数据写入文件句柄。                                         |
| `SetFilePointer()`/`SetFilePointerEx()` | 移动文件句柄的读写指针位置。                                   |
| `GetFileAttributes()`/`GetFileAttributesEx()` | 获取文件或目录的属性。                                       |
| `SetFileAttributes()`   | 设置文件或目录的属性。                                               |
| `CreateDirectory()`     | 创建一个新目录。                                                     |
| `RemoveDirectory()`     | 删除一个空目录。                                                     |
| `DeleteFile()`          | 删除一个文件。                                                       |
| `MoveFile()`/`MoveFileEx()` | 移动或重命名一个文件或目录。                                         |
| `CopyFile()`/`CopyFileEx()` | 复制一个文件。                                                       |
| `CreatePipe()`          | 创建一个匿名管道。                                                   |
| `CreateNamedPipe()`     | 创建一个命名管道。                                                   |
| `DeviceIoControl()`     | 向设备驱动程序发送控制代码。                                         |

### 3. 内存管理

| API 函数            | 描述                                                                   |
| ------------------- | ---------------------------------------------------------------------- |
| `VirtualAlloc()`    | 在调用进程的虚拟地址空间中保留或提交内存区域。                             |
| `VirtualFree()`     | 释放或解除提交先前分配的内存区域。                                       |
| `VirtualProtect()`  | 更改已提交内存区域的访问保护属性（如只读、可执行）。                       |
| `HeapAlloc()`       | 从进程的默认堆或私有堆中分配内存。                                       |
| `HeapFree()`        | 释放由 `HeapAlloc()` 分配的内存。                                          |
| `CreateFileMapping()` | 创建或打开一个文件映射对象（用于内存映射文件或进程间共享内存）。             |
| `MapViewOfFile()`   | 将文件映射对象的一部分或全部映射到调用进程的地址空间。                     |
| `UnmapViewOfFile()` | 从调用进程的地址空间取消映射先前映射的视图。                             |

### 4. 同步机制

| API 函数/对象类型 | 描述                                                                   |
| ----------------- | ---------------------------------------------------------------------- |
| `Mutex`           | 互斥体对象。`CreateMutex()`, `OpenMutex()`, `ReleaseMutex()`。               |
| `Semaphore`       | 信号量对象。`CreateSemaphore()`, `OpenSemaphore()`, `ReleaseSemaphore()`。   |
| `Event`           | 事件对象（用于线程间通知）。`CreateEvent()`, `SetEvent()`, `ResetEvent()`.    |
| `Critical Section`| 轻量级用户模式互斥机制。`InitializeCriticalSection()`, `EnterCriticalSection()`, `LeaveCriticalSection()`, `DeleteCriticalSection()`。 |
| `Interlocked*` 系列 | 提供原子操作（如增减、比较交换）。例如 `InterlockedIncrement()`, `InterlockedCompareExchange()`。 |

### 5. 网络 (Winsock API)

| API 函数      | 描述                                   |
| ------------- | -------------------------------------- |
| `WSAStartup()`  | 初始化 Winsock 库。                      |
| `WSACleanup()`| 清理 Winsock 库资源。                    |
| `socket()`    | 创建一个 socket 句柄。                   |
| `closesocket()`| 关闭一个 socket 句柄。                   |
| `bind()`      | 将 socket 绑定到本地地址。               |
| `listen()`    | 将 socket 置于监听状态。                 |
| `accept()`    | 接受一个传入连接。                     |
| `connect()`   | 发起一个连接。                         |
| `send()`/`WSASend()` | 发送数据。                             |
| `recv()`/`WSARecv()` | 接收数据。                             |
| `sendto()`/`WSASendTo()` | 发送 UDP 数据。                        |
| `recvfrom()`/`WSARecvFrom()` | 接收 UDP 数据。                        |
| `select()`/`WSAAsyncSelect()`/`WSAEventSelect()` | I/O 多路复用，检查多个 socket 的状态。 |

---

学习这些基础 API 是理解操作系统服务和进行系统级编程的关键一步。 