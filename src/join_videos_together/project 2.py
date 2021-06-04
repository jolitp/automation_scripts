#PY  <- Needed to identify #
#--automatically built--

adm = Avidemux()
if not adm.loadVideo("/home/jolitp/Projects/automation_scripts/src/join_videos_together/videos2/1_sec_VIDEO_1.mkv"):
    raise("Cannot load /home/jolitp/Projects/automation_scripts/src/join_videos_together/videos2/1_sec_VIDEO_1.mkv")
if not adm.appendVideo("/home/jolitp/Projects/automation_scripts/src/join_videos_together/videos2/1_sec_VIDEO_2.mkv"):
    raise("Cannot append /home/jolitp/Projects/automation_scripts/src/join_videos_together/videos2/1_sec_VIDEO_2.mkv")
if not adm.appendVideo("/home/jolitp/Projects/automation_scripts/src/join_videos_together/videos2/1_sec_VIDEO_3.mkv"):
    raise("Cannot append /home/jolitp/Projects/automation_scripts/src/join_videos_together/videos2/1_sec_VIDEO_3.mkv")
if not adm.appendVideo("/home/jolitp/Projects/automation_scripts/src/join_videos_together/videos2/1_sec_VIDEO_4.mkv"):
    raise("Cannot append /home/jolitp/Projects/automation_scripts/src/join_videos_together/videos2/1_sec_VIDEO_4.mkv")
if not adm.appendVideo("/home/jolitp/Projects/automation_scripts/src/join_videos_together/videos2/1_sec_VIDEO_5.mkv"):
    raise("Cannot append /home/jolitp/Projects/automation_scripts/src/join_videos_together/videos2/1_sec_VIDEO_5.mkv")
if not adm.appendVideo("/home/jolitp/Projects/automation_scripts/src/join_videos_together/videos2/1_sec_VIDEO_6.mkv"):
    raise("Cannot append /home/jolitp/Projects/automation_scripts/src/join_videos_together/videos2/1_sec_VIDEO_6.mkv")
if not adm.appendVideo("/home/jolitp/Projects/automation_scripts/src/join_videos_together/videos2/1_sec_VIDEO_7.mkv"):
    raise("Cannot append /home/jolitp/Projects/automation_scripts/src/join_videos_together/videos2/1_sec_VIDEO_7.mkv")
if not adm.appendVideo("/home/jolitp/Projects/automation_scripts/src/join_videos_together/videos2/1_sec_VIDEO_8.mkv"):
    raise("Cannot append /home/jolitp/Projects/automation_scripts/src/join_videos_together/videos2/1_sec_VIDEO_8.mkv")
if not adm.appendVideo("/home/jolitp/Projects/automation_scripts/src/join_videos_together/videos2/1_sec_VIDEO_9.mkv"):
    raise("Cannot append /home/jolitp/Projects/automation_scripts/src/join_videos_together/videos2/1_sec_VIDEO_9.mkv")
if not adm.appendVideo("/home/jolitp/Projects/automation_scripts/src/join_videos_together/videos2/1_sec_VIDEO_10.mkv"):
    raise("Cannot append /home/jolitp/Projects/automation_scripts/src/join_videos_together/videos2/1_sec_VIDEO_10.mkv")
adm.videoCodec("Copy")
adm.audioCodec(0, "copy")
adm.setContainer("MKV")
