# Django Ad Manager (BETA)

### An application that helps to manage, schedule and control [OpenX](http://www.openx.com/) ads from one server to another; intended for use on responsive webpages.

Tested and working with Djago 1.3.

---

#### SCHEMA

[![schema](https://raw.github.com/mhulse/django-ad-manager/master/ad_manager/ad_manager.png)](https://raw.github.com/mhulse/django-ad-manager/master/ad_manager/ad_manager.png)

---

#### EXAMPLE

##### URI:

```html
http://site.com/manager/entertainment:go-entertainment/section/?callback=baz
```

##### Where:

* <b>`manager`:</b> Django application name.
* <b>`entertainment:go-entertainment`:</b> Are `target` names (i.e. website sections and sub-sections) seperated by a colon. Minimum of one `target` required.
* <b>`section`:</b> Optional page type. If not defined, then all page types (for the group) are output.
* <b>`?callback=baz`:</b> JSONP `callback` name. If not defined, then the output will be a standard [JSON](http://www.json.org/) response.
* <b>`&cache=busted`:</b> Used to bust the Django `cache` (not shown in above exmaple).

##### [JSONP](http://en.wikipedia.org/wiki/JSONP) output:

```javascript
baz({
    "now": "2012-12-14 11:20",
    "target": [
        {
            "ad_group": [
                {
                    "ad": [
                        {
                            "ad_type": [
                                {
                                    "height": 90,
                                    "name": "Leaderboard",
                                    "slug": "leaderboard",
                                    "tag_type": "<iframe>",
                                    "width": 728
                                }
                            ],
                            "id": 322986
                        },
                        {
                            "ad_type": [
                                {
                                    "height": 50,
                                    "name": "Leaderboard",
                                    "slug": "leaderboard",
                                    "tag_type": "<iframe>",
                                    "width": 320
                                }
                            ],
                            "id": 322987
                        },
                        {
                            "ad_type": [
                                {
                                    "height": 250,
                                    "name": "Medium Rectangle 1",
                                    "slug": "medium-rectangle-1",
                                    "tag_type": "<iframe>",
                                    "width": 300
                                }
                            ],
                            "id": 322988
                        },
                        {
                            "ad_type": [
                                {
                                    "height": 250,
                                    "name": "Medium Rectangle 2",
                                    "slug": "medium-rectangle-2",
                                    "tag_type": "<iframe>",
                                    "width": 300
                                }
                            ],
                            "id": 322989
                        }
                    ],
                    "aug_id": 14055,
                    "page_type": "Section"
                }
            ],
            "name": "go Entertainment",
            "slug": "go-entertainment"
        },
        {
            "ad_group": [
                {
                    "ad": [
                        {
                            "ad_type": [
                                {
                                    "height": 60,
                                    "name": "Button",
                                    "slug": "button",
                                    "tag_type": "<iframe>",
                                    "width": 120
                                }
                            ],
                            "id": 327383
                        },
                        {
                            "ad_type": [
                                {
                                    "height": 60,
                                    "name": "Half Banner",
                                    "slug": "half-banner",
                                    "tag_type": "<iframe>",
                                    "width": 234
                                }
                            ],
                            "id": 328176
                        },
                        {
                            "ad_type": [
                                {
                                    "height": 250,
                                    "name": "Medium Rectangle 1",
                                    "slug": "medium-rectangle-1",
                                    "tag_type": "<iframe>",
                                    "width": 300
                                }
                            ],
                            "id": 278420
                        },
                        {
                            "ad_type": [
                                {
                                    "height": 90,
                                    "name": "Leaderboard",
                                    "slug": "leaderboard",
                                    "tag_type": "<iframe>",
                                    "width": 728
                                }
                            ],
                            "id": 328209
                        },
                        {
                            "ad_type": [
                                {
                                    "height": 50,
                                    "name": "Leaderboard",
                                    "slug": "leaderboard",
                                    "tag_type": "<iframe>",
                                    "width": 320
                                }
                            ],
                            "id": 328210
                        }
                    ],
                    "aug_id": 14229,
                    "page_type": ""
                }
            ],
            "name": "ROS",
            "slug": "ros"
        }
    ]
});
```

---

#### INSTALLATION

Install using [`pip`](http://www.pip-installer.org/):

```bash
$ sudo pip install -e git+https://github.com/mhulse/django-ad-manager.git#egg=django-ad-manager
```

Add `'ad_manager',` to your `installed_apps` setting.

Put this in your URLs:

```python
(r'^pages/', include('ad_manager.urls')),
```

Run:

```bash
$ sudo service apache2 restart
```

... or:

```bash
$ touch apache/django.wsgi
```

... or whatever you need to do to reload things.

Lastly:

```bash
$ python manage.py syncdb
```

... and you're ready to go (maybe do another `touch`?)!

Enjoy your **Django Ad Manager** app _today!_

---

#### LEGAL

Copyright &copy; 2013 [Micky Hulse](http://mky.io)

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this work except in compliance with the License. You may obtain a copy of the License in the LICENSE file, or at:

[http://www.apache.org/licenses/LICENSE-2.0](http://www.apache.org/licenses/LICENSE-2.0)

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
