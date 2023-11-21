from textx import metamodel_from_file

from BUML.metamodel.structural.structural import DomainModel
from BUML.notations.plantUML.plantuml_to_buml import plantuml_to_buml


# Testing TextX parsing of a simple domain concept
def test_textx_parsing():
    plantUML_mm = metamodel_from_file('src/BUML/notations/plantUML/plantuml.tx')
    hello_world_buml_model = plantUML_mm.model_from_file('tests/notations/hello_world.plantuml')
    assert len(hello_world_buml_model.elements) == 10
    # assert number of classes
    assert sum(1 if x.__class__.__name__ == 'Class' else 0 for x in hello_world_buml_model.elements) == 4
    # assert number of aggregation relationships
    assert sum(1 if x.__class__.__name__ == 'Aggregation' else 0 for x in hello_world_buml_model.elements) == 1
    # assert multiplicity of the BidirectionalDC relationship
    for rel in (rel for rel in hello_world_buml_model.elements if rel.__class__.__name__ == "Bidirectional"):
        if rel.name == "BidirectionalDC":
            assert rel.fromCar.min == 1
            assert rel.toCar.min == 1
            assert rel.toCar.max == '*'
    # assert visibility  of the attribute b2 of class B
    for cl in (cl for cl in hello_world_buml_model.elements if cl.__class__.__name__ == 'Class'):
        if cl == "B":
            for attr in (attr for attr in cl.classContents if attr.name == 'b2'):
                assert attr.visibility == '#'

# Testing Core model generation from TextX file
def test_plantuml_transformation():
    domain: DomainModel = plantuml_to_buml(model_path='tests/notations/hello_world.plantuml')
    # assert number of classes
    assert len(domain.get_classes()) == 4
    # assert number of aggregation associations
    assert len(domain.associations) == 3
    # assert that the CompositionAC relationship is composite
    for rel in domain.associations:
        if rel.name == "CompositionAC":
            assert list(rel.ends)[0].is_composite == True or list(rel.ends)[1].is_composite == True
    # assert number of generalizations
    assert len(domain.generalizations) == 2
    # assert number of constraints
    assert len(domain.constraints) == 2