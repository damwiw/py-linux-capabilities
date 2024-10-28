from enum import Enum

class LinuxCapabilities(Enum):
    CAP_AUDIT_CONTROL = "CAP_AUDIT_CONTROL"
    CAP_AUDIT_READ = "CAP_AUDIT_READ"
    CAP_AUDIT_WRITE = "CAP_AUDIT_WRITE"
    CAP_BLOCK_SUSPEND = "CAP_BLOCK_SUSPEND"
    CAP_BPF = "CAP_BPF"
    CAP_CHECKPOINT_RESTORE = "CAP_CHECKPOINT_RESTORE"
    CAP_CHOWN = "CAP_CHOWN"
    CAP_DAC_OVERRIDE = "CAP_DAC_OVERRIDE"
    CAP_DAC_READ_SEARCH = "CAP_DAC_READ_SEARCH"
    CAP_FOWNER = "CAP_FOWNER"
    CAP_FSETID = "CAP_FSETID"
    CAP_IPC_LOCK = "CAP_IPC_LOCK"
    CAP_IPC_OWNER = "CAP_IPC_OWNER"
    CAP_KILL = "CAP_KILL"
    CAP_LEASE = "CAP_LEASE"
    CAP_LINUX_IMMUTABLE = "CAP_LINUX_IMMUTABLE"
    CAP_MAC_ADMIN = "CAP_MAC_ADMIN"
    CAP_MAC_OVERRIDE = "CAP_MAC_OVERRIDE"
    CAP_MKNOD = "CAP_MKNOD"
    CAP_NET_ADMIN = "CAP_NET_ADMIN"
    CAP_NET_BIND_SERVICE = "CAP_NET_BIND_SERVICE"
    CAP_NET_BROADCAST = "CAP_NET_BROADCAST"
    CAP_NET_RAW = "CAP_NET_RAW"
    CAP_PERFMON = "CAP_PERFMON"
    CAP_SETFCAP = "CAP_SETFCAP"
    CAP_SETGID = "CAP_SETGID"
    CAP_SETPCAP = "CAP_SETPCAP"
    CAP_SETUID = "CAP_SETUID"
    CAP_SYS_ADMIN = "CAP_SYS_ADMIN"
    CAP_SYS_BOOT = "CAP_SYS_BOOT"
    CAP_SYS_CHROOT = "CAP_SYS_CHROOT"
    CAP_SYS_MODULE = "CAP_SYS_MODULE"
    CAP_SYS_NICE = "CAP_SYS_NICE"
    CAP_SYS_PACCT = "CAP_SYS_PACCT"
    CAP_SYS_PTRACE = "CAP_SYS_PTRACE"
    CAP_SYS_RAWIO = "CAP_SYS_RAWIO"
    CAP_SYS_RESOURCE = "CAP_SYS_RESOURCE"
    CAP_SYS_TIME = "CAP_SYS_TIME"
    CAP_SYS_TTY_CONFIG = "CAP_SYS_TTY_CONFIG"
    CAP_SYSLOG = "CAP_SYSLOG"
    CAP_WAKE_ALARM = "CAP_WAKE_ALARM"

