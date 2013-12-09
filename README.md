#Stradivarius
####An app for finding and booking professional musicians--powered by Python; built on Django and Mongo.




###ABOUT STRADIVARIUS

You can see a live example of the site at:

<http://concerttalent.com>

You must be a musician to register on the live site.  If you are a developer, e-mail the retainer for login info.


###TECHNOLOGY STACK
There are many ways to deploy Django.  Stradivarius uses: Django, mod_wsgi, and Apache installed on an AWS EC2 server (Ubuntu Precise 12.04-i386) associated with an Elastic IP. MongoDB is the database used in both development and production.  Site styling provided courtesy of Bootstrap.  All HTML5/CSS3 is fully validated.


###SETTINGS
With regard to Django settings, check out _The One True Way_ by Jacob Kaplan Moss:
<https://speakerdeck.com/jacobian/the-best-and-worst-of-django?slide=81>

Code is opinionated.  Here's an alternative to the above by Bruno Renié:
<http://bruno.im/2013/may/18/django-stop-writing-settings-files/>

Stradivarius' settings live in the _settings_ directory with separate files providing settings common to all environments ( _base.py_ ), as well as files providing settings unique to development ( _dev.py_ ), and production ( _prod.py_ ) environments.  Most settings are handled in this manner in accord with Kaplan Moss' "One True Way", but some are managed via environment variables and/or envdir in the manner prescribed by Renié.  Whenever possible, environment variables are set dynamically, outside of the settings.py.  Stradivarius' settings are still being optimized with the intent of enabling the aforementioned "Fast Lane" deployment on AWS, so--in the interim--some environment variables may need to be set manually.


You will need to change the following after launch...

In your Django settings file...
* ADMINS
* EMAIL_HOST_PASSWORD
* EMAIL_HOST_USER

In the .bashrc of your development machine...
* SECRET_KEY
* DEBUG

Set the SECRET_KEY and DEBUG as an environment variable on your development machine, like so...

    SECRET_KEY="your_secret_key"; export SECRET_KEY
    DEBUG="True"; export DEBUG

Or, make these settings permanent in your development environment via placing the following in ~/.bashrc, like so...

    export SECRET_KEY = 'your_secret_key'
    export DEBUG = 'True'

After adjusting these settings, remember to...

    touch .bashrc

If you're using a virtualenv--and you should-- _and_ you plan on running multiple environments on the same machine, you can place the above environment variable settings in your _bin/activate script_.  If you don't plan on running multiple environments on the same machine, just stick with placing the settings in the  _.bashrc_ file of your home directory.

Finally, if you use a different e-mail provider than Gmail, you'll have to provide additional e-mail info in Django's settings file.


###STATIC ASSETS VS. MEDIA FILES
As in other web frameworks,  "media" directories are traditionally reserved for files uploaded by users, and "static" is the label applied to resources related to styling the site. Django has its own conventions in this regard, and can get rather nuanced in its efforts to keep things tidy and loosely coupled between "apps" within a single overarching project.  Particularly, it's careful with regard to namespacing of static files, so that each Django app within a project can contain its own static assets (i.e., css, js, and img files) without name conflicts.  Django provides a convenience function--_collectstatic_--to gather all of these resources into a common directory (the "static" directory) and to reference them via a common URL.  (See: <https://docs.djangoproject.com/en/dev/howto/static-files/>)

Many beginning Djangonauts find this process and its nomenclature a bit confusing.  Stradivarius follows the convention of most Python and other web frameworks: it simply places all style related assets into one directory from the get go.  _Any_ file that has to do with styling of the site is labeled as "styles", and that's the directory in which you'll find it.  The "static" directory is empty--intentionally so--and should be left empty.  Manually placing files in the "static" directory will raise an ImproperlyConfigured exception. Presently, executing this command...

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


###TODO
* the virtualenv needs to be created with the --no-site-packages flag; this wasn't done on either the development machine nor the production machine, so the requirements.txt file may be a bit out of sync with regard to dependencies, and may require tweaking.
* view_one loads slowly; page caching helps after the page loads the first time, but perhaps it'd be nicer if the data were fetched asynchronously while displaying a throbber or progress bar.
* minor performance improvements might be enabled if static files were moved to S3 and retrieved from CloudFront CDN.


------------------------------------------------------------------------

###LICENSE

Copyright (c) 2013 by Sean Bradley.  All rights reserved.

If you're interested in using a fork of Stradivarius for commercial purposes, please contact the maintainer at:

sean@concerttalent.com