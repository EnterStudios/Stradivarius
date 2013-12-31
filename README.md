#Stradivarius
####An app for finding and booking professional musicians--powered by Python; built on Django and Mongo.


###ABOUT STRADIVARIUS

This is a work in progress, a pre-beta release. You can see the site live at:

<http://concerttalent.com>

You must be a professional musician to register on the live site. If you're a developer and want access, e-mail the repo's maintainer. (See below.)

###TECHNOLOGY STACK
Stradivarius is built on Django, mod_wsgi, and Apache installed on an AWS EC2 server (Ubuntu Precise 12.04-i386) associated with an Elastic IP. Site styling is provided courtesy of Bootstrap.  All HTML5/CSS3 is fully validated. Right now, the live site is simply a Flask-powered landing page. The code in this repo--which features fully functional authentication--presently relies on PostgreSQL. We're hurridly refactoring things to accommodate Mongo.


###JUST LOOKING FOR A REPO TO HELP YOU GET STARTED WITH DJANGO?
If you're just looking for a smart barebones project skeleton for your first your next Django project, especially if you plan on using **Heroku**, then checkout [django-skel] (https://github.com/rdegges/django-skel), or, alternatively, explore the exemplary [django-twoscoops-project] (https://github.com/twoscoops/django-twoscoops-project). If you're new to Django and plan on deploying to **AWS**, then you might prefer [Simpletown] (https://github.com/seanbradley/Simpletown). Simpletown not only clearly hints at best practices, but provides everything you need to launch a complete--albeit minimal and easy to wrangle--Django project on an Amazon EC2 instance.  Simpletown also comes with two example views--easy-to-understand functional views--one of which even fetches resources from an external API via Kenneth Reitz's awesome Requests library to get you started.


###SETTINGS
Stradivarius' settings live in its _settings_ directory with separate files providing settings common to all environments ( _base.py_ ), as well as files providing settings unique to development ( _dev.py_ ), and production ( _prod.py_ ) environments.  Most settings are handled in this manner in accord with Kaplan Moss' "One True Way" (See <https://speakerdeck.com/jacobian/the-best-and-worst-of-django?slide=81>), but some are managed via environment variables as suggested by the [django-twoscoops-project] (https://github.com/seanbradley/django-twoscoops-project).  Whenever possible, environment variables are set dynamically, outside of the settings.py.

Stradivarius' settings are still being optimized with the intent of enabling its rapid deployment on AWS, so--before you're able to simply replicate the site via an AWS snapshot--some environment variables may need to be set manually in in the _.bashrc_ file of your home directory. (Remember to _touch .bashrc_ afterwards if you do so.)  You can achieve a similar effect by setting environment variable at the end of your virtualenv's _bin/activate script_, which is usually found in the _~/.virtualenvs directory_ of whatever machine on which your installing the site.  Within the project's _settings_ directory, you'll also need to generate a _secret.py_ file containing Django's requisite SECRET_KEY. A utility script is included for that purpose.

Finally, if you use a different e-mail provider other than Gmail, you'll also have to provide additional e-mail info in Django's settings file.


###STATIC ASSETS VS. MEDIA FILES
As in other web frameworks,  "media" directories are traditionally reserved for files uploaded by users, and "static" is the label applied to resources related to styling the site. Django has its own conventions in this regard, and can get rather nuanced in its efforts to keep things tidy and loosely coupled between "apps" within a single overarching project.  Particularly, it's careful with regard to namespacing of static files, so that each Django app within a project can contain its own static assets (i.e., css, js, and img files) without name conflicts.  Django provides a convenience function--_collectstatic_--to gather all of these resources into a common directory (the "static" directory) and to reference them via a common URL.  (See: <https://docs.djangoproject.com/en/dev/howto/static-files/>)

Many beginning Djangonauts find this process and its nomenclature a bit confusing.  Stradivarius follows the convention of most Python and other web frameworks: it simply places all style related assets into one directory from the get go.  _Any_ file that has to do with styling of the site is labeled as "styles", and that's the directory in which you'll find it--the STYLES directory. If you have custom, global theming, that's where you should put it.  The traditional Django STATIC directory is empty--intentionally so--and should be left empty.  Manually placing files in the "static" directory will raise an ImproperlyConfigured exception. Presently, executing this command...

    ./manage.py collectstatic

...is still required to gather assets in the STYLE directory to the STATIC directory, and serve them up via the appropriate URL.

For styling related assets, Stradivarius provides the following directories...

styles<br />
....site-styles<br />
........css<br />
........img<br />
........js<br />
....admin-styles<br />
........css<br />
........img<br />
........js<br />


------------------------------------------------------------------------

###LICENSE AND CONTACT INFO

Copyright © 2013/2014 by Sean Bradley.

All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution. THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

If you're a developer interested in checking out the site, or interested in using a fork of Stradivarius for commercial purposes, please kindly give me a heads-up at:

sean@blogblimp.com