/* Copyright 2019 The TensorFlow Authors. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
==============================================================================*/

#include "model_settings.h"

const char* kCategoryLabels[kCategoryCount] = {
    "up","down","right","left","dclick",
};
/*to change number of pixels the curser jumps add number that number in with space to up, down... written above it should look like
const char* kCategoryLabels[kCategoryCount] = {
    "up 30","down 30","right 30","left 30","dclick 30",
}; the space is important*/
