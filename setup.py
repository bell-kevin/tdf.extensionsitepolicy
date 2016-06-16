from setuptools import setup, find_packages
import os

version = '1.0'

long_description = (
    open('README.txt').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.txt').read()
    + '\n' +
    open('CHANGES.txt').read()
    + '\n')

setup(name='tdf.extensionsitepolicy',
      version=version,
      description="The Plone policy add-on for the LibreOffice extensions site",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='Plone Add-On Policy LibreOffice Extensions Website',
      author='Andreas Mantke',
      author_email='maand@gmx.de',
      url='http://extensions.libreoffice.org',
      license='gpl',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['tdf', ],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Plone',
          'Pillow',
          'collective.psc.blobstorage',
          'tdf.liboextcenter',
          'collective.captcha',
          'quintagroup.plonecaptchas',
#          'Products.PloneFormGen',
          'tdf.libotemplatecenter',
          'collective.ATClamAV',
          'tdf.donateportlet',
#          'atreal.usersinout',
#          'zettwerk.users',
          'Products.LinguaPlone',
          'Products.DocFinderTab',
          'Products.ArchAddOn',
          'Products.AddRemoveWidget',
          'Products.DataGridField',
          'Products.PloneSoftwareCenter',
          'tdf.extensionsiteaccountform',
          'tdf.templatesiteaccountform',
          # -*- Extra requirements: -*-
          'collective.piwik.now',
          'collective.piwik.core',
          'collective.piwik.mediaelement',
          'collective.z3cform.norobots',
          'plone.app.dexterity[grok, relations]',
          'plone.app.multilingual[archetypes]==2.0.2',
      ],
      extras_require={'test': ['plone.app.testing']},
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
#      setup_requires=["PasteScript"],
#      paster_plugins=["templer.localcommands"],
      )
