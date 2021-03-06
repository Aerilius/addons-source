register(GRAMPLET,
         id="Face Detection",
         name=_("Face Detection"),
         description = _("Gramplet for detecting and assigning faces"),
         version = '1.0.19',
         gramps_target_version="5.1",
         status = UNSTABLE, # not yet tested with python 3
         fname="FaceDetection.py",
         height=200,
         gramplet = 'FaceDetection',
         gramplet_title=_("Faces"),
         navtypes=["Media"],
         )
