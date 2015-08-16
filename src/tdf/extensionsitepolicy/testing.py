from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting

from plone.testing import z2

from zope.configuration import xmlconfig


class TdfextensionsitepolicyLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import tdf.extensionsitepolicy
        xmlconfig.file(
            'configure.zcml',
            tdf.extensionsitepolicy,
            context=configurationContext
        )

        # Install products that use an old-style initialize() function
        #z2.installProduct(app, 'Products.PloneFormGen')

#    def tearDownZope(self, app):
#        # Uninstall products installed above
#        z2.uninstallProduct(app, 'Products.PloneFormGen')

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'tdf.extensionsitepolicy:default')

TDF_EXTENSIONSITEPOLICY_FIXTURE = TdfextensionsitepolicyLayer()
TDF_EXTENSIONSITEPOLICY_INTEGRATION_TESTING = IntegrationTesting(
    bases=(TDF_EXTENSIONSITEPOLICY_FIXTURE,),
    name="TdfextensionsitepolicyLayer:Integration"
)
