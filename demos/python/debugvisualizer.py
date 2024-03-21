from Person import Person
import json
from vscodedebugvisualizer import globalVisualizationFactory


class PersonVisualizer:
    def checkType(self, t):
        return isinstance(t, Person)

    def visualizePerson(self, person: Person, nodes=[], edges=[]):
        if person.name in [n["id"] for n in nodes]:
            return nodes, edges

        nodes.append(
            {
                "id": person.name,
                "label": person.name,
            }
        )

        for p in person.parents:
            nodes, edges = self.visualizePerson(p, nodes, edges)
            edges.append(
                {
                    "from": p.name,
                    "to": person.name,
                }
            )

        return nodes, edges

    def visualize(self, person: Person):
        jsonDict = {
            "kind": {"graph": True},
            "nodes": [],
            "edges": [],
        }

        self.visualizePerson(person, jsonDict["nodes"], jsonDict["edges"])

        # return json.dumps(jsonDict)
        # return '{"kind": {"plotly": true}, "data": [{"y": [1,2,3]}]}'
        return '{"data": [{"cells": {"values": [["(6,)"], [3.5], [6], [1]]}, "domain": {"x": [0.0, 1.0], "y": [0.0, 0.26666666666666666]}], "layout": {"xaxis": {"anchor": "y", "domain": [0.0, 1.0]}, "xaxis2": {"anchor": "y2", "domain": [0.0, 1.0]}, "yaxis": {"anchor": "x", "domain": [0.7333333333333334, 1.0]}, "yaxis2": {"anchor": "x2", "domain": [0.3666666666666667, 0.6333333333333333]}}, "kind": {"plotly": true}}'


globalVisualizationFactory.addVisualizer(PersonVisualizer())
