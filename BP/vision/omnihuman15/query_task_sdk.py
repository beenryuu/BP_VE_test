# coding:utf-8
from __future__ import print_function

from byteplus_sdk import visual
from byteplus_sdk.visual.VisualService import VisualService
import os

if __name__ == '__main__':
    visual_service = VisualService()

    # call below method if you don't set ak and sk in $HOME/.volc/config
    visual_service.set_ak(os.environ['BP_ACCESS_KEY'])
    visual_service.set_sk(os.environ['BP_SECRET_KEY'])
    
    # Request Body (Check interface documentation and copy the required parameters) 
    form = {
        "req_key": "realman_avatar_picture_omni15_cv",
        "task_id": os.environ['OMNI_TASK']
    }
    resp = visual_service.cv_get_result(form)
    print(resp)