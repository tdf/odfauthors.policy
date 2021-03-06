from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting

from plone.testing import z2

from zope.configuration import xmlconfig


class OdfauthorspolicyLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import odfauthors.policy
        xmlconfig.file(
            'configure.zcml',
            odfauthors.policy,
            context=configurationContext
        )

        # Install products that use an old-style initialize() function
        #z2.installProduct(app, 'Products.PloneFormGen')

#    def tearDownZope(self, app):
#        # Uninstall products installed above
#        z2.uninstallProduct(app, 'Products.PloneFormGen')

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'odfauthors.policy:default')

ODFAUTHORS_POLICY_FIXTURE = OdfauthorspolicyLayer()
ODFAUTHORS_POLICY_INTEGRATION_TESTING = IntegrationTesting(
    bases=(ODFAUTHORS_POLICY_FIXTURE,),
    name="OdfauthorspolicyLayer:Integration"
)
