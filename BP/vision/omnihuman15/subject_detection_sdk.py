# coding:utf-8
from __future__ import print_function

from byteplus_sdk import visual
from byteplus_sdk.visual.VisualService import VisualService
import os
import json

if __name__ == '__main__':
    visual_service = VisualService()

    # call below method if you don't set ak and sk in $HOME/.volc/config
    visual_service.set_ak(os.environ['BP_ACCESS_KEY'])
    visual_service.set_sk(os.environ['BP_SECRET_KEY'])
    
    # Request Body (Check interface documentation and copy the required parameters) 
    form = {
        "req_key": "realman_avatar_object_detection_cv",
        "image_url": os.environ['OMNI_IMAGE']
    }
    
    resp = visual_service.cv_process(form)['data']['resp_data']
    print(json.loads(resp))