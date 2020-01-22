#!/usr/bin/env python
from urllib import request
import unittest
import os

BASEURL = "http://127.0.0.1:8080"

class TestYourWebserver(unittest.TestCase):
    def setUp(self,baseurl=BASEURL):
        """do nothing"""
        self.baseurl = baseurl

    # def test_get_404(self):
    #     url = self.baseurl + "/do-not-implement-this-page-it-is-not-found"
    #     try:
    #         req = request.urlopen(url, None, 3)
    #         self.assertTrue( False, "Should have thrown an HTTP Error!")
    #     except request.HTTPError as e:
    #         self.assertTrue( e.getcode()  == 404 , ("404 Not FOUND! %d" % e.getcode()))
    #     else:
    #         self.assertTrue( False, "Another Error was thrown!")


    # CMPUT404W19 did not have to pass to this
    def test_deep_no_end(self):
        url = self.baseurl + "/deep"
        expected_url = self.baseurl + "/deep/"
        try:
            req = request.urlopen(url, None, 3)
            code = req.getcode()
            if code >= 200 and code <= 299 and req.geturl() == expected_url:
                 self.assertTrue(True, "The library has redirected for us")
            else:
                self.assertTrue(False, "The URL hasn't changed %s %s" % (code,req.geturl()))
        except request.HTTPError as e:
            code = e.getcode()
            self.assertTrue( code >= 300 and code < 400, "300ish Not FOUND! %s" % code)
    #
    # def test_hardcode2(self):
    #     url = self.baseurl + "/deep.css"
    #     try:
    #         req = request.urlopen(url, None, 3)
    #         self.assertTrue( False, "Should have thrown an HTTP Error for /deep.css!")
    #     except request.HTTPError as e:
    #         self.assertTrue( e.getcode()  == 404 , ("404 Not FOUND! %d" % e.getcode()))
    #     else:
    #         self.assertTrue( False, "Another Error was thrown!")
    #     url = self.baseurl + "/deep/deep"
    #     try:
    #         req = request.urlopen(url, None, 3)
    #         self.assertTrue( False, "Should have thrown an HTTP Error for /deep/deep!")
    #     except request.HTTPError as e:
    #         self.assertTrue( e.getcode()  == 404 , ("404 Not FOUND! %d" % e.getcode()))
    #     else:
    #         self.assertTrue( False, "Another Error was thrown!")

if __name__ == '__main__':
    unittest.main()
