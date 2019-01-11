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
from fhir.resources import observation
from fhir.resources.fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class ObservationTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Observation", js["resourceType"])
        return observation.Observation(js)
    
    def testObservation1(self):
        inst = self.instantiate_from("observation-example-date-lastmp.json")
        self.assertIsNotNone(inst, "Must have instantiated a Observation instance")
        self.implObservation1(inst)
        
        js = inst.as_json()
        self.assertEqual("Observation", js["resourceType"])
        inst2 = observation.Observation(js)
        self.implObservation1(inst2)
    
    def implObservation1(self, inst):
        self.assertEqual(inst.category[0].coding[0].code, "survey")
        self.assertEqual(inst.category[0].coding[0].display, "Survey")
        self.assertEqual(inst.category[0].coding[0].system, "http://hl7.org/fhir/observation-category")
        self.assertEqual(inst.category[0].text, "AOE")
        self.assertEqual(inst.code.coding[0].code, "8665-2")
        self.assertEqual(inst.code.coding[0].display, "Date last menstrual period")
        self.assertEqual(inst.code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.code.text, "Date last menstrual period")
        self.assertEqual(inst.effectiveDateTime.date, FHIRDate("2016-01-24").date)
        self.assertEqual(inst.effectiveDateTime.as_json(), "2016-01-24")
        self.assertEqual(inst.id, "date-lastmp")
        self.assertEqual(inst.status, "final")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.valueDateTime.date, FHIRDate("2016-12-30").date)
        self.assertEqual(inst.valueDateTime.as_json(), "2016-12-30")
    
    def testObservation2(self):
        inst = self.instantiate_from("observation-example-body-temperature.json")
        self.assertIsNotNone(inst, "Must have instantiated a Observation instance")
        self.implObservation2(inst)
        
        js = inst.as_json()
        self.assertEqual("Observation", js["resourceType"])
        inst2 = observation.Observation(js)
        self.implObservation2(inst2)
    
    def implObservation2(self, inst):
        self.assertEqual(inst.category[0].coding[0].code, "vital-signs")
        self.assertEqual(inst.category[0].coding[0].display, "Vital Signs")
        self.assertEqual(inst.category[0].coding[0].system, "http://hl7.org/fhir/observation-category")
        self.assertEqual(inst.category[0].text, "Vital Signs")
        self.assertEqual(inst.code.coding[0].code, "8310-5")
        self.assertEqual(inst.code.coding[0].display, "Body temperature")
        self.assertEqual(inst.code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.code.text, "Body temperature")
        self.assertEqual(inst.effectiveDateTime.date, FHIRDate("1999-07-02").date)
        self.assertEqual(inst.effectiveDateTime.as_json(), "1999-07-02")
        self.assertEqual(inst.id, "body-temperature")
        self.assertEqual(inst.meta.profile[0], "http://hl7.org/fhir/StructureDefinition/vitalsigns")
        self.assertEqual(inst.status, "final")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.valueQuantity.code, "Cel")
        self.assertEqual(inst.valueQuantity.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.valueQuantity.unit, "C")
        self.assertEqual(inst.valueQuantity.value, 36.5)
    
    def testObservation3(self):
        inst = self.instantiate_from("observation-example-phenotype.json")
        self.assertIsNotNone(inst, "Must have instantiated a Observation instance")
        self.implObservation3(inst)
        
        js = inst.as_json()
        self.assertEqual("Observation", js["resourceType"])
        inst2 = observation.Observation(js)
        self.implObservation3(inst2)
    
    def implObservation3(self, inst):
        self.assertEqual(inst.code.coding[0].code, "79716-7")
        self.assertEqual(inst.code.coding[0].display, "CYP2C9 gene product metabolic activity interpretation")
        self.assertEqual(inst.code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.extension[0].url, "http://hl7.org/fhir/StructureDefinition/observation-geneticsGene")
        self.assertEqual(inst.extension[0].valueCodeableConcept.coding[0].code, "2623")
        self.assertEqual(inst.extension[0].valueCodeableConcept.coding[0].display, "CYP2C9")
        self.assertEqual(inst.extension[0].valueCodeableConcept.coding[0].system, "http://www.genenames.org")
        self.assertEqual(inst.id, "example-phenotype")
        self.assertEqual(inst.issued.date, FHIRDate("2013-04-03T15:30:10+01:00").date)
        self.assertEqual(inst.issued.as_json(), "2013-04-03T15:30:10+01:00")
        self.assertEqual(inst.related[0].type, "derived-from")
        self.assertEqual(inst.status, "final")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.valueCodeableConcept.coding[0].code, "LA25391-6")
        self.assertEqual(inst.valueCodeableConcept.coding[0].display, "Normal metabolizer")
        self.assertEqual(inst.valueCodeableConcept.coding[0].system, "http://loinc.org")
    
    def testObservation4(self):
        inst = self.instantiate_from("observation-example-2minute-apgar-score.json")
        self.assertIsNotNone(inst, "Must have instantiated a Observation instance")
        self.implObservation4(inst)
        
        js = inst.as_json()
        self.assertEqual("Observation", js["resourceType"])
        inst2 = observation.Observation(js)
        self.implObservation4(inst2)
    
    def implObservation4(self, inst):
        self.assertEqual(inst.category[0].coding[0].code, "survey")
        self.assertEqual(inst.category[0].coding[0].display, "Survey")
        self.assertEqual(inst.category[0].coding[0].system, "http://hl7.org/fhir/observation-category")
        self.assertEqual(inst.category[0].text, "Survey")
        self.assertEqual(inst.code.coding[0].code, "9273-4")
        self.assertEqual(inst.code.coding[0].display, "2 minute Apgar Score")
        self.assertEqual(inst.code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.code.text, "2 minute Apgar Score")
        self.assertEqual(inst.component[0].code.coding[0].code, "249227004")
        self.assertEqual(inst.component[0].code.coding[0].display, "Apgar color score")
        self.assertEqual(inst.component[0].code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.component[0].code.text, "Apgar color score")
        self.assertEqual(inst.component[0].valueCodeableConcept.coding[0].code, "LA6723-6")
        self.assertEqual(inst.component[0].valueCodeableConcept.coding[0].display, "Good color in body with bluish hands or feet")
        self.assertEqual(inst.component[0].valueCodeableConcept.coding[0].extension[0].url, "http://hl7.org/fhir/StructureDefinition/iso21090-CO-value")
        self.assertEqual(inst.component[0].valueCodeableConcept.coding[0].extension[0].valueDecimal, 1)
        self.assertEqual(inst.component[0].valueCodeableConcept.coding[0].system, "http://loinc.org/la")
        self.assertEqual(inst.component[0].valueCodeableConcept.coding[1].code, "1")
        self.assertEqual(inst.component[0].valueCodeableConcept.coding[1].system, "http:/acme.ped/apgarcolor")
        self.assertEqual(inst.component[0].valueCodeableConcept.text, "1. Good color in body with bluish hands or feet")
        self.assertEqual(inst.component[1].code.coding[0].code, "249223000")
        self.assertEqual(inst.component[1].code.coding[0].display, "Apgar heart rate score")
        self.assertEqual(inst.component[1].code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.component[1].code.text, "Apgar respiratory effort score")
        self.assertEqual(inst.component[1].valueCodeableConcept.coding[0].code, "LA6720-2")
        self.assertEqual(inst.component[1].valueCodeableConcept.coding[0].display, "Fewer than 100 beats per minute")
        self.assertEqual(inst.component[1].valueCodeableConcept.coding[0].extension[0].url, "http://hl7.org/fhir/StructureDefinition/iso21090-CO-value")
        self.assertEqual(inst.component[1].valueCodeableConcept.coding[0].extension[0].valueDecimal, 1)
        self.assertEqual(inst.component[1].valueCodeableConcept.coding[0].system, "http://loinc.org/la")
        self.assertEqual(inst.component[1].valueCodeableConcept.coding[1].code, "1")
        self.assertEqual(inst.component[1].valueCodeableConcept.coding[1].system, "http:/acme.ped/apgarheartrate")
        self.assertEqual(inst.component[1].valueCodeableConcept.text, "1. Fewer than 100 beats per minute")
        self.assertEqual(inst.component[2].code.coding[0].code, "249226008")
        self.assertEqual(inst.component[2].code.coding[0].display, "Apgar response to stimulus score")
        self.assertEqual(inst.component[2].code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.component[2].code.text, "Apgar response to stimulus score")
        self.assertEqual(inst.component[2].valueCodeableConcept.coding[0].code, "LA6721-0")
        self.assertEqual(inst.component[2].valueCodeableConcept.coding[0].display, "Grimace during suctioning")
        self.assertEqual(inst.component[2].valueCodeableConcept.coding[0].extension[0].url, "http://hl7.org/fhir/StructureDefinition/iso21090-CO-value")
        self.assertEqual(inst.component[2].valueCodeableConcept.coding[0].extension[0].valueDecimal, 1)
        self.assertEqual(inst.component[2].valueCodeableConcept.coding[0].system, "http://loinc.org/la")
        self.assertEqual(inst.component[2].valueCodeableConcept.coding[1].code, "1")
        self.assertEqual(inst.component[2].valueCodeableConcept.coding[1].system, "http:/acme.ped/apgarreflexirritability")
        self.assertEqual(inst.component[2].valueCodeableConcept.text, "1. Grimace during suctioning")
        self.assertEqual(inst.component[3].code.coding[0].code, "249225007")
        self.assertEqual(inst.component[3].code.coding[0].display, "Apgar muscle tone score")
        self.assertEqual(inst.component[3].code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.component[3].code.text, "Apgar muscle tone score")
        self.assertEqual(inst.component[3].valueCodeableConcept.coding[0].code, "LA6714-5")
        self.assertEqual(inst.component[3].valueCodeableConcept.coding[0].display, "Some flexion of arms and legs")
        self.assertEqual(inst.component[3].valueCodeableConcept.coding[0].extension[0].url, "http://hl7.org/fhir/StructureDefinition/iso21090-CO-value")
        self.assertEqual(inst.component[3].valueCodeableConcept.coding[0].extension[0].valueDecimal, 1)
        self.assertEqual(inst.component[3].valueCodeableConcept.coding[0].system, "http://loinc.org/la")
        self.assertEqual(inst.component[3].valueCodeableConcept.coding[1].code, "1")
        self.assertEqual(inst.component[3].valueCodeableConcept.coding[1].system, "http:/acme.ped/apgarmuscletone")
        self.assertEqual(inst.component[3].valueCodeableConcept.text, "1. Some flexion of arms and legs")
        self.assertEqual(inst.component[4].code.coding[0].code, "249224006")
        self.assertEqual(inst.component[4].code.coding[0].display, "Apgar respiratory effort score")
        self.assertEqual(inst.component[4].code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.component[4].code.text, "Apgar respiratory effort score")
        self.assertEqual(inst.component[4].valueCodeableConcept.coding[0].code, "LA6726-9")
        self.assertEqual(inst.component[4].valueCodeableConcept.coding[0].display, "Weak cry; may sound like whimpering, slow or irregular breathing")
        self.assertEqual(inst.component[4].valueCodeableConcept.coding[0].extension[0].url, "http://hl7.org/fhir/StructureDefinition/iso21090-CO-value")
        self.assertEqual(inst.component[4].valueCodeableConcept.coding[0].extension[0].valueDecimal, 1)
        self.assertEqual(inst.component[4].valueCodeableConcept.coding[0].system, "http://loinc.org/la")
        self.assertEqual(inst.component[4].valueCodeableConcept.coding[1].code, "1")
        self.assertEqual(inst.component[4].valueCodeableConcept.coding[1].system, "http:/acme.ped/apgarrespiratoryeffort")
        self.assertEqual(inst.component[4].valueCodeableConcept.text, "1. Weak cry; may sound like whimpering, slow or irregular breathing")
        self.assertEqual(inst.contained[0].id, "newborn")
        self.assertEqual(inst.effectiveDateTime.date, FHIRDate("2016-05-18T22:33:22Z").date)
        self.assertEqual(inst.effectiveDateTime.as_json(), "2016-05-18T22:33:22Z")
        self.assertEqual(inst.id, "2minute-apgar-score")
        self.assertEqual(inst.status, "final")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.valueQuantity.code, "{score}")
        self.assertEqual(inst.valueQuantity.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.valueQuantity.value, 5)
    
    def testObservation5(self):
        inst = self.instantiate_from("observation-example-f202-temperature.json")
        self.assertIsNotNone(inst, "Must have instantiated a Observation instance")
        self.implObservation5(inst)
        
        js = inst.as_json()
        self.assertEqual("Observation", js["resourceType"])
        inst2 = observation.Observation(js)
        self.implObservation5(inst2)
    
    def implObservation5(self, inst):
        self.assertEqual(inst.bodySite.coding[0].code, "74262004")
        self.assertEqual(inst.bodySite.coding[0].display, "Oral cavity")
        self.assertEqual(inst.bodySite.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.category[0].coding[0].code, "vital-signs")
        self.assertEqual(inst.category[0].coding[0].display, "Vital Signs")
        self.assertEqual(inst.category[0].coding[0].system, "http://hl7.org/fhir/observation-category")
        self.assertEqual(inst.code.coding[0].code, "BT")
        self.assertEqual(inst.code.coding[0].display, "Body temperature")
        self.assertEqual(inst.code.coding[0].system, "http://acme.lab")
        self.assertEqual(inst.code.coding[1].code, "8310-5")
        self.assertEqual(inst.code.coding[1].display, "Body temperature")
        self.assertEqual(inst.code.coding[1].system, "http://loinc.org")
        self.assertEqual(inst.code.coding[2].code, "8331-1")
        self.assertEqual(inst.code.coding[2].display, "Oral temperature")
        self.assertEqual(inst.code.coding[2].system, "http://loinc.org")
        self.assertEqual(inst.code.coding[3].code, "56342008")
        self.assertEqual(inst.code.coding[3].display, "Temperature taking")
        self.assertEqual(inst.code.coding[3].system, "http://snomed.info/sct")
        self.assertEqual(inst.code.text, "Temperature")
        self.assertEqual(inst.id, "f202")
        self.assertEqual(inst.interpretation.coding[0].code, "H")
        self.assertEqual(inst.interpretation.coding[0].system, "http://hl7.org/fhir/v2/0078")
        self.assertEqual(inst.issued.date, FHIRDate("2013-04-04T13:27:00+01:00").date)
        self.assertEqual(inst.issued.as_json(), "2013-04-04T13:27:00+01:00")
        self.assertEqual(inst.method.coding[0].code, "89003005")
        self.assertEqual(inst.method.coding[0].display, "Oral temperature taking")
        self.assertEqual(inst.method.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.referenceRange[0].high.unit, "degrees C")
        self.assertEqual(inst.referenceRange[0].high.value, 38.2)
        self.assertEqual(inst.status, "entered-in-error")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.valueQuantity.code, "Cel")
        self.assertEqual(inst.valueQuantity.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.valueQuantity.unit, "degrees C")
        self.assertEqual(inst.valueQuantity.value, 39)
    
    def testObservation6(self):
        inst = self.instantiate_from("observation-example-haplotype1.json")
        self.assertIsNotNone(inst, "Must have instantiated a Observation instance")
        self.implObservation6(inst)
        
        js = inst.as_json()
        self.assertEqual("Observation", js["resourceType"])
        inst2 = observation.Observation(js)
        self.implObservation6(inst2)
    
    def implObservation6(self, inst):
        self.assertEqual(inst.code.coding[0].code, "55233-1")
        self.assertEqual(inst.code.coding[0].display, "Genetic analysis master panel-- This is the parent OBR for the panel holding all of the associated observations that can be reported with a molecular genetics analysis result.")
        self.assertEqual(inst.code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.extension[0].url, "http://hl7.org/fhir/StructureDefinition/observation-geneticsGene")
        self.assertEqual(inst.extension[0].valueCodeableConcept.coding[0].code, "2625")
        self.assertEqual(inst.extension[0].valueCodeableConcept.coding[0].display, "CYP2D6")
        self.assertEqual(inst.extension[0].valueCodeableConcept.coding[0].system, "http://www.genenames.org")
        self.assertEqual(inst.extension[1].url, "http://hl7.org/fhir/StructureDefinition/observation-geneticsSequence")
        self.assertEqual(inst.extension[2].url, "http://hl7.org/fhir/StructureDefinition/observation-geneticsSequence")
        self.assertEqual(inst.id, "example-haplotype1")
        self.assertEqual(inst.issued.date, FHIRDate("2013-04-03T15:30:10+01:00").date)
        self.assertEqual(inst.issued.as_json(), "2013-04-03T15:30:10+01:00")
        self.assertEqual(inst.related[0].type, "derived-from")
        self.assertEqual(inst.related[1].type, "derived-from")
        self.assertEqual(inst.status, "unknown")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.valueCodeableConcept.coding[0].code, "PA165971587")
        self.assertEqual(inst.valueCodeableConcept.coding[0].display, "*35B")
        self.assertEqual(inst.valueCodeableConcept.coding[0].system, "http://pharmakb.org")
    
    def testObservation7(self):
        inst = self.instantiate_from("observation-example-vitals-panel.json")
        self.assertIsNotNone(inst, "Must have instantiated a Observation instance")
        self.implObservation7(inst)
        
        js = inst.as_json()
        self.assertEqual("Observation", js["resourceType"])
        inst2 = observation.Observation(js)
        self.implObservation7(inst2)
    
    def implObservation7(self, inst):
        self.assertEqual(inst.category[0].coding[0].code, "vital-signs")
        self.assertEqual(inst.category[0].coding[0].display, "Vital Signs")
        self.assertEqual(inst.category[0].coding[0].system, "http://hl7.org/fhir/observation-category")
        self.assertEqual(inst.category[0].text, "Vital Signs")
        self.assertEqual(inst.code.coding[0].code, "85353-1")
        self.assertEqual(inst.code.coding[0].display, "Vital signs, weight, height, head circumference, oxygen saturation and BMI panel")
        self.assertEqual(inst.code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.code.text, "Vital signs Panel")
        self.assertEqual(inst.effectiveDateTime.date, FHIRDate("1999-07-02").date)
        self.assertEqual(inst.effectiveDateTime.as_json(), "1999-07-02")
        self.assertEqual(inst.id, "vitals-panel")
        self.assertEqual(inst.meta.profile[0], "http://hl7.org/fhir/StructureDefinition/vitalsigns")
        self.assertEqual(inst.related[0].type, "has-member")
        self.assertEqual(inst.related[1].type, "has-member")
        self.assertEqual(inst.related[2].type, "has-member")
        self.assertEqual(inst.related[3].type, "has-member")
        self.assertEqual(inst.status, "final")
        self.assertEqual(inst.text.status, "generated")
    
    def testObservation8(self):
        inst = self.instantiate_from("observation-example-mbp.json")
        self.assertIsNotNone(inst, "Must have instantiated a Observation instance")
        self.implObservation8(inst)
        
        js = inst.as_json()
        self.assertEqual("Observation", js["resourceType"])
        inst2 = observation.Observation(js)
        self.implObservation8(inst2)
    
    def implObservation8(self, inst):
        self.assertEqual(inst.category[0].coding[0].code, "vital-signs")
        self.assertEqual(inst.category[0].coding[0].display, "Vital Signs")
        self.assertEqual(inst.category[0].coding[0].system, "http://hl7.org/fhir/observation-category")
        self.assertEqual(inst.category[0].text, "Vital Signs")
        self.assertEqual(inst.code.coding[0].code, "8478-0")
        self.assertEqual(inst.code.coding[0].display, "Mean blood pressure")
        self.assertEqual(inst.code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.code.text, "Mean blood pressure")
        self.assertEqual(inst.effectiveDateTime.date, FHIRDate("1999-07-02").date)
        self.assertEqual(inst.effectiveDateTime.as_json(), "1999-07-02")
        self.assertEqual(inst.id, "mbp")
        self.assertEqual(inst.status, "final")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.valueQuantity.code, "mm[Hg]")
        self.assertEqual(inst.valueQuantity.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.valueQuantity.unit, "mm[Hg]")
        self.assertEqual(inst.valueQuantity.value, 80)
    
    def testObservation9(self):
        inst = self.instantiate_from("observation-example-head-circumference.json")
        self.assertIsNotNone(inst, "Must have instantiated a Observation instance")
        self.implObservation9(inst)
        
        js = inst.as_json()
        self.assertEqual("Observation", js["resourceType"])
        inst2 = observation.Observation(js)
        self.implObservation9(inst2)
    
    def implObservation9(self, inst):
        self.assertEqual(inst.category[0].coding[0].code, "vital-signs")
        self.assertEqual(inst.category[0].coding[0].display, "Vital Signs")
        self.assertEqual(inst.category[0].coding[0].system, "http://hl7.org/fhir/observation-category")
        self.assertEqual(inst.category[0].text, "Vital Signs")
        self.assertEqual(inst.code.coding[0].code, "8287-5")
        self.assertEqual(inst.code.coding[0].display, "Head Occipital-frontal circumference by Tape measure")
        self.assertEqual(inst.code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.code.text, "Head Circumference")
        self.assertEqual(inst.effectiveDateTime.date, FHIRDate("1999-07-02").date)
        self.assertEqual(inst.effectiveDateTime.as_json(), "1999-07-02")
        self.assertEqual(inst.id, "head-circumference")
        self.assertEqual(inst.meta.profile[0], "http://hl7.org/fhir/StructureDefinition/vitalsigns")
        self.assertEqual(inst.status, "final")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.valueQuantity.code, "cm")
        self.assertEqual(inst.valueQuantity.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.valueQuantity.unit, "cm")
        self.assertEqual(inst.valueQuantity.value, 51.2)
    
    def testObservation10(self):
        inst = self.instantiate_from("observation-example-respiratory-rate.json")
        self.assertIsNotNone(inst, "Must have instantiated a Observation instance")
        self.implObservation10(inst)
        
        js = inst.as_json()
        self.assertEqual("Observation", js["resourceType"])
        inst2 = observation.Observation(js)
        self.implObservation10(inst2)
    
    def implObservation10(self, inst):
        self.assertEqual(inst.category[0].coding[0].code, "vital-signs")
        self.assertEqual(inst.category[0].coding[0].display, "Vital Signs")
        self.assertEqual(inst.category[0].coding[0].system, "http://hl7.org/fhir/observation-category")
        self.assertEqual(inst.category[0].text, "Vital Signs")
        self.assertEqual(inst.code.coding[0].code, "9279-1")
        self.assertEqual(inst.code.coding[0].display, "Respiratory rate")
        self.assertEqual(inst.code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.code.text, "Respiratory rate")
        self.assertEqual(inst.effectiveDateTime.date, FHIRDate("1999-07-02").date)
        self.assertEqual(inst.effectiveDateTime.as_json(), "1999-07-02")
        self.assertEqual(inst.id, "respiratory-rate")
        self.assertEqual(inst.meta.profile[0], "http://hl7.org/fhir/StructureDefinition/vitalsigns")
        self.assertEqual(inst.status, "final")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.valueQuantity.code, "/min")
        self.assertEqual(inst.valueQuantity.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.valueQuantity.unit, "breaths/minute")
        self.assertEqual(inst.valueQuantity.value, 26)

