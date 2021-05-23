#PY  <- Needed to identify #
#--automatically built--

adm = Avidemux()
if not adm.loadVideo("/home/jolitp/Projects/automation_scripts/src/get_videos_info_csv/Want To Kick The Habit  Quit WindowsToday!-jschFelwsiI.webm"):
    raise("Cannot load /home/jolitp/Projects/automation_scripts/src/get_videos_info_csv/Want To Kick The Habit  Quit WindowsToday!-jschFelwsiI.webm")
if not adm.appendVideo("/home/jolitp/Projects/automation_scripts/src/get_videos_info_csv/What's The Best 'Linux'  It's GNU_Linux!-UcckLr4fQQs.webm"):
    raise("Cannot append /home/jolitp/Projects/automation_scripts/src/get_videos_info_csv/What's The Best 'Linux'  It's GNU_Linux!-UcckLr4fQQs.webm")
if not adm.appendVideo("/home/jolitp/Projects/automation_scripts/src/get_videos_info_csv/Why I Choose Free And Open Source Software-cU6H2m9XuQY.webm"):
    raise("Cannot append /home/jolitp/Projects/automation_scripts/src/get_videos_info_csv/Why I Choose Free And Open Source Software-cU6H2m9XuQY.webm")
if not adm.appendVideo("/home/jolitp/Projects/automation_scripts/src/get_videos_info_csv/Why I'm Thankful This Holiday Season-6H1QKXbY9qk.webm"):
    raise("Cannot append /home/jolitp/Projects/automation_scripts/src/get_videos_info_csv/Why I'm Thankful This Holiday Season-6H1QKXbY9qk.webm")
if not adm.appendVideo("/home/jolitp/Projects/automation_scripts/src/get_videos_info_csv/Why Use Mac When Linux Exists-KEWJFP_kHeo.webm"):
    raise("Cannot append /home/jolitp/Projects/automation_scripts/src/get_videos_info_csv/Why Use Mac When Linux Exists-KEWJFP_kHeo.webm")
adm.videoCodec("Copy")
adm.audioCodec(0, "copy")
adm.setContainer("MKV")
