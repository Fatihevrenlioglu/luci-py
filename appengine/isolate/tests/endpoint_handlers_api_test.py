#!/usr/bin/env python
# Copyright 2014 The Swarming Authors. All rights reserved.
# Use of this source code is governed by the Apache v2.0 license that can be
# found in the LICENSE file.

import json
import logging
import sys
import unittest

import test_env
test_env.setup_test_env()

import dev_appserver
dev_appserver.fix_sys_path()

import endpoints
from protorpc.remote import protojson
from support import test_case

import webtest

from components import auth_testing
from contextlib import contextmanager
import endpoint_handlers_api
from endpoint_handlers_api import Digest
from endpoint_handlers_api import DigestCollection


class IsolateServiceTest(test_case.EndpointsTestCase):
  """Test the IsolateService's API methods."""
  # TODO(cmassaro): this should eventually inherit from endpointstestcase

  def setUp(self):
    super(IsolateServiceTest, self).setUp()
    auth_testing.mock_get_current_identity(self)
    self.testbed.setup_env(current_version_id='testbed.version')
    self.testbed.init_all_stubs()
    self.source_ip = '127.0.0.1'
    self.app_api = webtest.TestApp(
        endpoints.api_server([endpoint_handlers_api.IsolateService],
                             restricted=False),
        extra_environ={'REMOTE_ADDR': self.source_ip})

  @classmethod
  def message_to_dict(cls, message):
    """Returns a JSON-ish dictionary corresponding to the RPC message."""
    return json.loads(protojson.encode_message(message))

  def test_pre_upload_ok(self):
    """Assert that preupload correctly posts the DigestCollection."""
    good_digests = DigestCollection(items=[Digest(digest='abcd', size=4)])
    bad_1 = DigestCollection(items=[Digest(digest='g', size=4)])
    bad_2 = DigestCollection(items=[Digest(digest='abcd', size=400)],
                             namespace='~whatever')

    url = '/_ah/spi/IsolateService.preupload'
    response = self.app_api.post_json(url,
                                      self.message_to_dict(good_digests))
    self.assertNotEqual(response, None)
    # TODO(cmassaro): change the above pending URL generation implementation
    with self.call_should_fail('400'):
      response = self.app_api.post_json(url, self.message_to_dict(bad_1))
    with self.call_should_fail('400'):
      response = self.app_api.post_json(url, self.message_to_dict(bad_2))


if __name__ == '__main__':
  if '-v' in sys.argv:
    unittest.TestCase.maxDiff = None
    logging.basicConfig(level=logging.DEBUG)
  else:
    logging.basicConfig(level=logging.FATAL)
  unittest.main()
