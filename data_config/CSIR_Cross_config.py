# -*- coding: utf-8 -*-
"""
configuration of iris test
RenMin20191024
"""

class Config(object):
    def __init__(self):
        # type of pretrain-model
        self.model_name = 'maxoutBN'
        # image path
        self._root_path = []
        self._train_list = []
        self._num_class = []
        self._normalize = []   
        ####################### training dataset #########################     
        # 00 Bath
        self._root_path.append('../../00Bath/')
        self._train_list.append('../../00Bath/Imglist.txt')
        self._num_class.append(99)
        self._normalize.append(dict(mean=0.3381,std=0.0796))
        # 01 ICE
        self._root_path.append('../../01ICE/')
        self._train_list.append('../../01ICE/Imglist.txt')
        self._num_class.append(175)
        self._normalize.append(dict(mean=0.4387,std=0.2549))
        # 02 CASIAIRIS
        self._root_path.append('../../02CASIAIRIS/')
        self._train_list.append('../../02CASIAIRIS/Imglist.txt')
        self._num_class.append(2786)
        self._normalize.append(dict(mean=0.4226,std=0.2769))
        # 03 NDCrossSensor        
        self._root_path.append('../../03NDCrossSensor/')
        self._train_list.append('../../03NDCrossSensor/Imglist.txt')
        self._num_class.append(1352)
        self._normalize.append(dict(mean=0.4426,std=0.2447))
        # 04 CSIR
        # ---------------------
        # 05 MobileV2_data
        self._root_path.append('../../05MobileV2/')
        self._train_list.append('../../05MobileV2/Imglist.txt')
        self._num_class.append(400)
        self._normalize.append(dict(mean=0.3632,std=0.1688))
        # 06 CASIA-Interval
        self._root_path.append('../../06CASIA-Iris-Interval/')
        self._train_list.append('../../06CASIA-Iris-Interval/Imglist.txt')
        self._num_class.append(366)
        self._normalize.append(dict(mean=0.6120,std=0.1161))        
        # 07 CASIA-Lamp
        self._root_path.append('../../07CASIA-Iris-Lamp/')
        self._train_list.append('../../07CASIA-Iris-Lamp/Imglist.txt')
        self._num_class.append(819)
        self._normalize.append(dict(mean=0.3506,std=0.1371))
        # 08 CASIA-Thousand
        self._root_path.append('../../08CASIA-Iris-Thousand/')
        self._train_list.append('../../08CASIA-Iris-Thousand/Imglist.txt')
        self._num_class.append(2000)
        self._normalize.append(dict(mean=0.2930,std=0.0843))        
        # 09 CASIA-Distance
        self._root_path.append('../../09CASIA-Iris-Distance/')
        self._train_list.append('../../09CASIA-Iris-Distance/Imglist.txt')
        self._num_class.append(284)
        self._normalize.append(dict(mean=0.2930,std=0.0843))

        ####################### within dataset #########################
        # 



        ####################### testing dataset #########################
        # test set
        # CSIR
        self._root_path_gallery = ['../../04CSIR/']
        self._gallery_list = ['../../04CSIR/test_gallery.txt']

        self._root_path_probe = ['../../04CSIR/']
        self._probe_list = ['../../04CSIR/test_probe.txt']

        self.data_name = 'CASIA Cross-sensor'
        self.test_type = 'Cross'
        
    def num_classGet(self):
        return self._num_class

    def load_detailGet(self):
        return self._root_path, self._train_list

    def gallery_loaderGet(self):
        return  self._root_path_gallery, self._gallery_list
    def probe_loaderGet(self):
        return  self._root_path_probe, self._probe_list