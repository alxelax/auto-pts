"""GAP test cases"""

try:
    from ptsprojects.testcase import TestCase, TestCmd, TestFunc, \
        TestFuncCleanUp
    from ptsprojects.zephyr.qtestcase import QTestCase

except ImportError: # running this module as script
    import sys
    sys.path.append("../..") # to be able to locate the following imports

    from ptsprojects.testcase import TestCase, TestCmd, TestFunc, \
        TestFuncCleanUp
    from ptsprojects.zephyr.qtestcase import QTestCase

from ptsprojects.zephyr.iutctl import get_zephyr
from msgdefs import *

def test_cases():
    """Returns a list of GAP test cases
    pts -- Instance of PyPTS"""

    zephyrctl = get_zephyr()

    test_cases = [
        QTestCase("GAP", "TC_CONN_CPUP_BV_01_C",
                  [TestFunc(zephyrctl.sock_send, SERVICE_ID['SERVICE_ID_CORE'], CORE_SERVICE_OP['OP_REGISTER_SERVICE'],
                            (SERVICE_ID['SERVICE_ID_GAP'],) ),
                   TestFunc(zephyrctl.sock_read, SERVICE_ID['SERVICE_ID_CORE'], CORE_SERVICE_OP['OP_REGISTER_SERVICE'],
                            None),
                   TestFunc(zephyrctl.sock_send, SERVICE_ID['SERVICE_ID_GAP'], GAP_SERVICE_OP['OP_GAP_START_ADV'],
                            (ADV_TYPE['ADV_IND'],) ),
                  ]),
        QTestCase("GAP", "TC_CONN_CPUP_BV_02_C",
                  [TestFunc(zephyrctl.sock_send, SERVICE_ID['SERVICE_ID_CORE'], CORE_SERVICE_OP['OP_REGISTER_SERVICE'],
                            (SERVICE_ID['SERVICE_ID_GAP'],) ),
                   TestFunc(zephyrctl.sock_read, SERVICE_ID['SERVICE_ID_CORE'], CORE_SERVICE_OP['OP_REGISTER_SERVICE'],
                            None),
                   TestFunc(zephyrctl.sock_send, SERVICE_ID['SERVICE_ID_GAP'], GAP_SERVICE_OP['OP_GAP_START_ADV'],
                            (ADV_TYPE['ADV_IND'],) ),
                  ]),
        QTestCase("GAP", "TC_CONN_CPUP_BV_03_C",
                  [TestFunc(zephyrctl.sock_send, SERVICE_ID['SERVICE_ID_CORE'], CORE_SERVICE_OP['OP_REGISTER_SERVICE'],
                            (SERVICE_ID['SERVICE_ID_GAP'],) ),
                   TestFunc(zephyrctl.sock_read, SERVICE_ID['SERVICE_ID_CORE'], CORE_SERVICE_OP['OP_REGISTER_SERVICE'],
                            None),
                   TestFunc(zephyrctl.sock_send, SERVICE_ID['SERVICE_ID_GAP'], GAP_SERVICE_OP['OP_GAP_START_ADV'],
                            (ADV_TYPE['ADV_IND'],) ),
                  ]),
        QTestCase("GAP", "TC_CONN_UCON_BV_01_C",
                  [TestFunc(zephyrctl.sock_send, SERVICE_ID['SERVICE_ID_CORE'], CORE_SERVICE_OP['OP_REGISTER_SERVICE'],
                            (SERVICE_ID['SERVICE_ID_GAP'],) ),
                   TestFunc(zephyrctl.sock_read, SERVICE_ID['SERVICE_ID_CORE'], CORE_SERVICE_OP['OP_REGISTER_SERVICE'],
                            None),
                   TestFunc(zephyrctl.sock_send, SERVICE_ID['SERVICE_ID_GAP'], GAP_SERVICE_OP['OP_GAP_START_ADV'],
                            (ADV_TYPE['ADV_IND'],) ),
                  ]),
        QTestCase("GAP", "TC_DISC_NONM_BV_02_C",
                  [TestFunc(zephyrctl.sock_send, SERVICE_ID['SERVICE_ID_CORE'], CORE_SERVICE_OP['OP_REGISTER_SERVICE'],
                            (SERVICE_ID['SERVICE_ID_GAP'],) ),
                   TestFunc(zephyrctl.sock_read, SERVICE_ID['SERVICE_ID_CORE'], CORE_SERVICE_OP['OP_REGISTER_SERVICE'],
                            None),
                   TestFunc(zephyrctl.sock_send, SERVICE_ID['SERVICE_ID_GAP'], GAP_SERVICE_OP['OP_GAP_START_ADV'],
                            (ADV_TYPE['ADV_IND'],) ),
                  ]),
        QTestCase("GAP", "TC_CONN_UCON_BV_02_C",
                  [TestFunc(zephyrctl.sock_send, SERVICE_ID['SERVICE_ID_CORE'], CORE_SERVICE_OP['OP_REGISTER_SERVICE'],
                            (SERVICE_ID['SERVICE_ID_GAP'],) ),
                   TestFunc(zephyrctl.sock_read, SERVICE_ID['SERVICE_ID_CORE'], CORE_SERVICE_OP['OP_REGISTER_SERVICE'],
                            None),
                   TestFunc(zephyrctl.sock_send, SERVICE_ID['SERVICE_ID_GAP'], GAP_SERVICE_OP['OP_GAP_START_ADV'],
                            (ADV_TYPE['ADV_IND'],) ),
                  ]),
        #TODO No needed implementation of setting discoverable mode
        #QTestCase("GAP", "TC_DISC_GENM_BV_04_C"),
        QTestCase("GAP", "TC_DISC_NONM_BV_01_C",
                  [TestFunc(zephyrctl.sock_send, SERVICE_ID['SERVICE_ID_CORE'], CORE_SERVICE_OP['OP_REGISTER_SERVICE'],
                            (SERVICE_ID['SERVICE_ID_GAP'],) ),
                   TestFunc(zephyrctl.sock_read, SERVICE_ID['SERVICE_ID_CORE'], CORE_SERVICE_OP['OP_REGISTER_SERVICE'],
                            None),
                   TestFunc(zephyrctl.sock_send, SERVICE_ID['SERVICE_ID_GAP'], GAP_SERVICE_OP['OP_GAP_START_ADV'],
                            (ADV_TYPE['ADV_NONCONN_IND'],) ),
                  ]),
        QTestCase("GAP", "TC_CONN_NCON_BV_01_C",
                  [TestFunc(zephyrctl.sock_send, SERVICE_ID['SERVICE_ID_CORE'], CORE_SERVICE_OP['OP_REGISTER_SERVICE'],
                            (SERVICE_ID['SERVICE_ID_GAP'],) ),
                   TestFunc(zephyrctl.sock_read, SERVICE_ID['SERVICE_ID_CORE'], CORE_SERVICE_OP['OP_REGISTER_SERVICE'],
                            None),
                   TestFunc(zephyrctl.sock_send, SERVICE_ID['SERVICE_ID_GAP'], GAP_SERVICE_OP['OP_GAP_START_ADV'],
                            (ADV_TYPE['ADV_NONCONN_IND'],) ),
                  ]),
        #TODO No support to set flags in adv data
        #QTestCase("GAP", "TC_ADV_BV_03_C"),
        #TODO Mandatory GAP services missing on IUT
        #QTestCase("GAP", "TC_GAT_BV_01_C"),
        #TODO implementation of ZEPHYR disconnect is needed
        #QTestCase("GAP", "TC_CONN_TERM_BV_01_C"),
    ]

    return test_cases

def main():
    """Main."""
    import sys
    import ptsprojects.zephyr.iutctl as iutctl

    # to be able to successfully create ZephyrCtl in QTestCase
    iutctl.ZEPHYR_KERNEL_IMAGE = sys.argv[0]

    test_cases_ = test_cases()

    for test_case in test_cases_:
        print
        print test_case
        for index, cmd in enumerate(test_case.cmds):
            print "%d) %s" % (index, cmd)

if __name__ == "__main__":
    main()