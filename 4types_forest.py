############################################################## 1 #######################################################
# class Forest:
#     _life_is_like_a_box_of: str = 'chocolate'
#
#      def__init__(self):                                                          #__init__(self):                      (1)
#         self.life_is_like_a_box_of = Forest._life_is_like_a_box_of                 # self.life_is = Forest._life_is
#
# mama_said = Forest()
# print(mama_said._life_is_like_a_box_of)                                                            # prints: chocolate
#
############################################################## 2 #######################################################
# class Forest:
#     _life_is_like_a_box_of: str = 'chocolate'
#                                                                                                                        (2)
# mama_said = Forest()
# print(mama_said._life_is_like_a_box_of)                                                            # prints: chocolate
#
############################################################## 3 #######################################################
# class Forest:
#     _life_is_like_a_box_of: str = 'chocolate'
#
#     def get_life_is_like_a_box_of(self):                                         # get life_is(self):
#         return self._life_is_like_a_box_of                                         # return self._life_is              (3)
#
# mama_said = Forest()
# print(mama_said.get_life_is_like_a_box_of())      #ניגש דרך הפונקציה לכן יש סוגריים בסוף#          # prints: chocolate
#
############################################################## 4 #######################################################
# class Forest:
#     _life_is_like_a_box_of: str = 'chocolate'
#
#     @property                                                                  # @property
#     def get_life_is_like_a_box_of(self):                                        # get life_is(self):
#         return self._life_is_like_a_box_of                                        # return self._life_is               (4)
#
# mama_said = Forest()
# print(mama_said.get_life_is_like_a_box_of)    #ניגש דרך הפונקציה אך ללא סוגריים בגלל הפרופרטי#     # prints: chocolate
#
########################################################################################################################

