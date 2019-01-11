#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.1.11917 on 2019-01-11.
#  2019, SMART Health IT.

import os
import pytest
import io
import unittest
import json
from fhir.resources import appointmentresponse
from fhir.resources.fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class AppointmentResponseTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("AppointmentResponse", js["resourceType"])
        return appointmentresponse.AppointmentResponse(js)
    
    def testAppointmentResponse1(self):
        inst = self.instantiate_from("appointmentresponse-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a AppointmentResponse instance")
        self.implAppointmentResponse1(inst)
        
        js = inst.as_json()
        self.assertEqual("AppointmentResponse", js["resourceType"])
        inst2 = appointmentresponse.AppointmentResponse(js)
        self.implAppointmentResponse1(inst2)
    
    def implAppointmentResponse1(self, inst):
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.participantStatus, "accepted")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">Accept Brian MRI results discussion</div>")
        self.assertEqual(inst.text.status, "generated")
    
    def testAppointmentResponse2(self):
        inst = self.instantiate_from("appointmentresponse-example-req.json")
        self.assertIsNotNone(inst, "Must have instantiated a AppointmentResponse instance")
        self.implAppointmentResponse2(inst)
        
        js = inst.as_json()
        self.assertEqual("AppointmentResponse", js["resourceType"])
        inst2 = appointmentresponse.AppointmentResponse(js)
        self.implAppointmentResponse2(inst2)
    
    def implAppointmentResponse2(self, inst):
        self.assertEqual(inst.comment, "can't we try for this time, can't do mornings")
        self.assertEqual(inst.end.date, FHIRDate("2013-12-25T13:30:00Z").date)
        self.assertEqual(inst.end.as_json(), "2013-12-25T13:30:00Z")
        self.assertEqual(inst.id, "exampleresp")
        self.assertEqual(inst.identifier[0].system, "http://example.org/sampleappointmentresponse-identifier")
        self.assertEqual(inst.identifier[0].value, "response123")
        self.assertEqual(inst.participantStatus, "tentative")
        self.assertEqual(inst.participantType[0].coding[0].code, "ATND")
        self.assertEqual(inst.participantType[0].coding[0].system, "http://hl7.org/fhir/v3/ParticipationType")
        self.assertEqual(inst.start.date, FHIRDate("2013-12-25T13:15:00Z").date)
        self.assertEqual(inst.start.as_json(), "2013-12-25T13:15:00Z")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">Accept Brian MRI results discussion</div>")
        self.assertEqual(inst.text.status, "generated")

