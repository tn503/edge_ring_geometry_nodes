import bpy
import mathutils
import os
import typing


# Import node groups from Blender essentials library
datafiles_path = bpy.utils.system_resource('DATAFILES')
lib_relpath = "assets/nodes/geometry_nodes_essentials.blend"
lib_path = os.path.join(datafiles_path, lib_relpath)
with bpy.data.libraries.load(lib_path, link=True)  as (data_src, data_dst):
	data_dst.node_groups = []
	if "Curve to Tube" in data_src.node_groups:
		data_dst.node_groups.append("Curve to Tube")
	if "Is Edge Boundary" in data_src.node_groups:
		data_dst.node_groups.append("Is Edge Boundary")
	if "Is Edge Boundary" in data_src.node_groups:
		data_dst.node_groups.append("Is Edge Boundary")
	if "Is Edge Boundary" in data_src.node_groups:
		data_dst.node_groups.append("Is Edge Boundary")
	if "Is Edge Boundary" in data_src.node_groups:
		data_dst.node_groups.append("Is Edge Boundary")


def geometry_nodes_1_node_group(node_tree_names: dict[typing.Callable, str]):
    """Initialize Geometry Nodes node group"""
    geometry_nodes_1 = bpy.data.node_groups.new(type='GeometryNodeTree', name="Geometry Nodes")

    geometry_nodes_1.color_tag = 'NONE'
    geometry_nodes_1.description = ""
    geometry_nodes_1.default_group_node_width = 140
    geometry_nodes_1.is_modifier = True
    geometry_nodes_1.show_modifier_manage_panel = True

    # geometry_nodes_1 interface

    # Socket Geometry
    geometry_socket = geometry_nodes_1.interface.new_socket(name="Geometry", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    geometry_socket.attribute_domain = 'POINT'
    geometry_socket.default_input = 'VALUE'
    geometry_socket.structure_type = 'AUTO'

    # Socket Geometry
    geometry_socket_1 = geometry_nodes_1.interface.new_socket(name="Geometry", in_out='INPUT', socket_type='NodeSocketGeometry')
    geometry_socket_1.attribute_domain = 'POINT'
    geometry_socket_1.default_input = 'VALUE'
    geometry_socket_1.structure_type = 'AUTO'

    # Initialize geometry_nodes_1 nodes

    # Node Group Input
    group_input = geometry_nodes_1.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"

    # Node Group Output
    group_output = geometry_nodes_1.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.is_active_output = True

    # Node Join Geometry
    join_geometry = geometry_nodes_1.nodes.new("GeometryNodeJoinGeometry")
    join_geometry.name = "Join Geometry"

    # Node Integer
    integer = geometry_nodes_1.nodes.new("FunctionNodeInputInt")
    integer.name = "Integer"
    integer.integer = 132

    # Node Sample Index.003
    sample_index_003 = geometry_nodes_1.nodes.new("GeometryNodeSampleIndex")
    sample_index_003.name = "Sample Index.003"
    sample_index_003.clamp = False
    sample_index_003.data_type = 'FLOAT_VECTOR'
    sample_index_003.domain = 'EDGE'

    # Node Edge Vertices
    edge_vertices = geometry_nodes_1.nodes.new("GeometryNodeInputMeshEdgeVertices")
    edge_vertices.name = "Edge Vertices"

    # Node Vector Math
    vector_math = geometry_nodes_1.nodes.new("ShaderNodeVectorMath")
    vector_math.name = "Vector Math"
    vector_math.operation = 'ADD'

    # Node Vector Math.001
    vector_math_001 = geometry_nodes_1.nodes.new("ShaderNodeVectorMath")
    vector_math_001.name = "Vector Math.001"
    vector_math_001.operation = 'SCALE'
    # Scale
    vector_math_001.inputs[3].default_value = 0.5

    # Node Mesh to Curve
    mesh_to_curve = geometry_nodes_1.nodes.new("GeometryNodeMeshToCurve")
    mesh_to_curve.name = "Mesh to Curve"
    mesh_to_curve.mode = 'EDGES'

    # Node Curve to Tube
    curve_to_tube = geometry_nodes_1.nodes.new("GeometryNodeGroup")
    curve_to_tube.name = "Curve to Tube"
    # Finding linked library node group
    for node_group in bpy.data.node_groups:
        if (
            node_group.name == "Curve to Tube"
            and node_group.bl_idname == 'GeometryNodeTree'
        ):
            curve_to_tube.node_tree = node_group
    if curve_to_tube.node_tree is None:
        print("Couldn't find node group Curve to Tube, failing")
        return
    # Socket_5
    curve_to_tube.inputs[1].default_value = 0.009999999776482582
    # Socket_4
    curve_to_tube.inputs[2].default_value = 'Round'
    # Socket_26
    curve_to_tube.inputs[3].default_value = 'Object'
    # Socket_2
    curve_to_tube.inputs[6].default_value = 8
    # Socket_11
    curve_to_tube.inputs[7].default_value = True
    # Socket_36
    curve_to_tube.inputs[8].default_value = True
    # Socket_32
    curve_to_tube.inputs[9].default_value = 'Evaluated'
    # Socket_33
    curve_to_tube.inputs[10].default_value = 10
    # Socket_37
    curve_to_tube.inputs[11].default_value = 0.10000000149011612
    # Socket_38
    curve_to_tube.inputs[12].default_value = 1.0
    # Socket_39
    curve_to_tube.inputs[13].default_value = True
    # Socket_10
    curve_to_tube.inputs[14].default_value = 'Flat'
    # Socket_25
    curve_to_tube.inputs[15].default_value = 'Object'
    # Socket_28
    curve_to_tube.inputs[20].default_value = 12
    # Socket_15
    curve_to_tube.inputs[21].default_value = False
    # Socket_13
    curve_to_tube.inputs[22].default_value = True
    # Socket_14
    curve_to_tube.inputs[23].default_value = False
    # Socket_30
    curve_to_tube.inputs[24].default_value = True
    # Socket_31
    curve_to_tube.inputs[25].default_value = True
    # Socket_17
    curve_to_tube.inputs[26].default_value = "UVMap"
    # Socket_19
    curve_to_tube.inputs[27].default_value = 'Length'
    # Socket_20
    curve_to_tube.inputs[28].default_value = 'Factor'
    # Socket_29
    curve_to_tube.inputs[29].default_value = True

    # Node Set Material
    set_material = geometry_nodes_1.nodes.new("GeometryNodeSetMaterial")
    set_material.name = "Set Material"
    # Selection
    set_material.inputs[1].default_value = True

    # Node Repeat Input.003
    repeat_input_003 = geometry_nodes_1.nodes.new("GeometryNodeRepeatInput")
    repeat_input_003.name = "Repeat Input.003"
    # Node Repeat Output.003
    repeat_output_003 = geometry_nodes_1.nodes.new("GeometryNodeRepeatOutput")
    repeat_output_003.name = "Repeat Output.003"
    repeat_output_003.active_index = 2
    repeat_output_003.inspection_index = 0
    repeat_output_003.repeat_items.clear()
    # Create item "Geometry"
    repeat_output_003.repeat_items.new('GEOMETRY', "Geometry")
    # Create item "edge_index1"
    repeat_output_003.repeat_items.new('INT', "edge_index1")
    # Create item "edge_index2"
    repeat_output_003.repeat_items.new('INT', "edge_index2")
    # Create item "Geometry.001"
    repeat_output_003.repeat_items.new('GEOMETRY', "Geometry.001")
    # Create item "Iteration"
    repeat_output_003.repeat_items.new('INT', "Iteration")
    # Item_3
    repeat_output_003.inputs[4].default_value = 0

    # Node Sample Index.006
    sample_index_006 = geometry_nodes_1.nodes.new("GeometryNodeSampleIndex")
    sample_index_006.name = "Sample Index.006"
    sample_index_006.clamp = False
    sample_index_006.data_type = 'INT'
    sample_index_006.domain = 'EDGE'

    # Node Corners of Edge.002
    corners_of_edge_002 = geometry_nodes_1.nodes.new("GeometryNodeCornersOfEdge")
    corners_of_edge_002.name = "Corners of Edge.002"
    # Edge Index
    corners_of_edge_002.inputs[0].default_value = 0
    # Weights
    corners_of_edge_002.inputs[1].default_value = 0.0
    # Sort Index
    corners_of_edge_002.inputs[2].default_value = 0

    # Node Offset Corner in Face.004
    offset_corner_in_face_004 = geometry_nodes_1.nodes.new("GeometryNodeOffsetCornerInFace")
    offset_corner_in_face_004.name = "Offset Corner in Face.004"
    # Offset
    offset_corner_in_face_004.inputs[1].default_value = 3

    # Node Offset Corner in Face.005
    offset_corner_in_face_005 = geometry_nodes_1.nodes.new("GeometryNodeOffsetCornerInFace")
    offset_corner_in_face_005.name = "Offset Corner in Face.005"
    # Offset
    offset_corner_in_face_005.inputs[1].default_value = 2

    # Node Vertex of Corner.005
    vertex_of_corner_005 = geometry_nodes_1.nodes.new("GeometryNodeVertexOfCorner")
    vertex_of_corner_005.name = "Vertex of Corner.005"
    vertex_of_corner_005.hide = True

    # Node Vertex of Corner.006
    vertex_of_corner_006 = geometry_nodes_1.nodes.new("GeometryNodeVertexOfCorner")
    vertex_of_corner_006.name = "Vertex of Corner.006"
    vertex_of_corner_006.hide = True

    # Node Compare.010
    compare_010 = geometry_nodes_1.nodes.new("FunctionNodeCompare")
    compare_010.name = "Compare.010"
    compare_010.hide = True
    compare_010.data_type = 'INT'
    compare_010.mode = 'ELEMENT'
    compare_010.operation = 'EQUAL'

    # Node Boolean Math.006
    boolean_math_006 = geometry_nodes_1.nodes.new("FunctionNodeBooleanMath")
    boolean_math_006.name = "Boolean Math.006"
    boolean_math_006.operation = 'AND'

    # Node Compare.011
    compare_011 = geometry_nodes_1.nodes.new("FunctionNodeCompare")
    compare_011.name = "Compare.011"
    compare_011.hide = True
    compare_011.data_type = 'INT'
    compare_011.mode = 'ELEMENT'
    compare_011.operation = 'EQUAL'

    # Node Edge Vertices.006
    edge_vertices_006 = geometry_nodes_1.nodes.new("GeometryNodeInputMeshEdgeVertices")
    edge_vertices_006.name = "Edge Vertices.006"

    # Node Compare.012
    compare_012 = geometry_nodes_1.nodes.new("FunctionNodeCompare")
    compare_012.name = "Compare.012"
    compare_012.hide = True
    compare_012.data_type = 'INT'
    compare_012.mode = 'ELEMENT'
    compare_012.operation = 'EQUAL'

    # Node Boolean Math.007
    boolean_math_007 = geometry_nodes_1.nodes.new("FunctionNodeBooleanMath")
    boolean_math_007.name = "Boolean Math.007"
    boolean_math_007.operation = 'AND'

    # Node Compare.013
    compare_013 = geometry_nodes_1.nodes.new("FunctionNodeCompare")
    compare_013.name = "Compare.013"
    compare_013.hide = True
    compare_013.data_type = 'INT'
    compare_013.mode = 'ELEMENT'
    compare_013.operation = 'EQUAL'

    # Node Boolean Math.008
    boolean_math_008 = geometry_nodes_1.nodes.new("FunctionNodeBooleanMath")
    boolean_math_008.name = "Boolean Math.008"
    boolean_math_008.operation = 'OR'

    # Node Attribute Statistic.001
    attribute_statistic_001 = geometry_nodes_1.nodes.new("GeometryNodeAttributeStatistic")
    attribute_statistic_001.name = "Attribute Statistic.001"
    attribute_statistic_001.data_type = 'FLOAT'
    attribute_statistic_001.domain = 'EDGE'

    # Node Index.003
    index_003 = geometry_nodes_1.nodes.new("GeometryNodeInputIndex")
    index_003.name = "Index.003"

    # Node Duplicate Elements.001
    duplicate_elements_001 = geometry_nodes_1.nodes.new("GeometryNodeDuplicateElements")
    duplicate_elements_001.name = "Duplicate Elements.001"
    duplicate_elements_001.domain = 'EDGE'
    # Amount
    duplicate_elements_001.inputs[2].default_value = 1

    # Node Set Position.001
    set_position_001 = geometry_nodes_1.nodes.new("GeometryNodeSetPosition")
    set_position_001.name = "Set Position.001"
    # Selection
    set_position_001.inputs[1].default_value = True
    # Position
    set_position_001.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Offset
    set_position_001.inputs[3].default_value = (0.0, 0.0, 0.0)

    # Node Join Geometry.003
    join_geometry_003 = geometry_nodes_1.nodes.new("GeometryNodeJoinGeometry")
    join_geometry_003.name = "Join Geometry.003"

    # Node Sample Index.007
    sample_index_007 = geometry_nodes_1.nodes.new("GeometryNodeSampleIndex")
    sample_index_007.name = "Sample Index.007"
    sample_index_007.clamp = False
    sample_index_007.data_type = 'INT'
    sample_index_007.domain = 'EDGE'

    # Node Corners of Edge.003
    corners_of_edge_003 = geometry_nodes_1.nodes.new("GeometryNodeCornersOfEdge")
    corners_of_edge_003.name = "Corners of Edge.003"
    # Edge Index
    corners_of_edge_003.inputs[0].default_value = 0
    # Weights
    corners_of_edge_003.inputs[1].default_value = 0.0
    # Sort Index
    corners_of_edge_003.inputs[2].default_value = 1

    # Node Offset Corner in Face.006
    offset_corner_in_face_006 = geometry_nodes_1.nodes.new("GeometryNodeOffsetCornerInFace")
    offset_corner_in_face_006.name = "Offset Corner in Face.006"
    # Offset
    offset_corner_in_face_006.inputs[1].default_value = 3

    # Node Offset Corner in Face.007
    offset_corner_in_face_007 = geometry_nodes_1.nodes.new("GeometryNodeOffsetCornerInFace")
    offset_corner_in_face_007.name = "Offset Corner in Face.007"
    # Offset
    offset_corner_in_face_007.inputs[1].default_value = 2

    # Node Vertex of Corner.007
    vertex_of_corner_007 = geometry_nodes_1.nodes.new("GeometryNodeVertexOfCorner")
    vertex_of_corner_007.name = "Vertex of Corner.007"
    vertex_of_corner_007.hide = True

    # Node Vertex of Corner.008
    vertex_of_corner_008 = geometry_nodes_1.nodes.new("GeometryNodeVertexOfCorner")
    vertex_of_corner_008.name = "Vertex of Corner.008"
    vertex_of_corner_008.hide = True

    # Node Compare.015
    compare_015 = geometry_nodes_1.nodes.new("FunctionNodeCompare")
    compare_015.name = "Compare.015"
    compare_015.hide = True
    compare_015.data_type = 'INT'
    compare_015.mode = 'ELEMENT'
    compare_015.operation = 'EQUAL'

    # Node Boolean Math.009
    boolean_math_009 = geometry_nodes_1.nodes.new("FunctionNodeBooleanMath")
    boolean_math_009.name = "Boolean Math.009"
    boolean_math_009.operation = 'AND'

    # Node Compare.016
    compare_016 = geometry_nodes_1.nodes.new("FunctionNodeCompare")
    compare_016.name = "Compare.016"
    compare_016.hide = True
    compare_016.data_type = 'INT'
    compare_016.mode = 'ELEMENT'
    compare_016.operation = 'EQUAL'

    # Node Edge Vertices.007
    edge_vertices_007 = geometry_nodes_1.nodes.new("GeometryNodeInputMeshEdgeVertices")
    edge_vertices_007.name = "Edge Vertices.007"

    # Node Compare.017
    compare_017 = geometry_nodes_1.nodes.new("FunctionNodeCompare")
    compare_017.name = "Compare.017"
    compare_017.hide = True
    compare_017.data_type = 'INT'
    compare_017.mode = 'ELEMENT'
    compare_017.operation = 'EQUAL'

    # Node Boolean Math.010
    boolean_math_010 = geometry_nodes_1.nodes.new("FunctionNodeBooleanMath")
    boolean_math_010.name = "Boolean Math.010"
    boolean_math_010.operation = 'AND'

    # Node Compare.018
    compare_018 = geometry_nodes_1.nodes.new("FunctionNodeCompare")
    compare_018.name = "Compare.018"
    compare_018.hide = True
    compare_018.data_type = 'INT'
    compare_018.mode = 'ELEMENT'
    compare_018.operation = 'EQUAL'

    # Node Boolean Math.011
    boolean_math_011 = geometry_nodes_1.nodes.new("FunctionNodeBooleanMath")
    boolean_math_011.name = "Boolean Math.011"
    boolean_math_011.operation = 'OR'

    # Node Boolean Math
    boolean_math = geometry_nodes_1.nodes.new("FunctionNodeBooleanMath")
    boolean_math.name = "Boolean Math"
    boolean_math.operation = 'OR'

    # Node Sample Index.008
    sample_index_008 = geometry_nodes_1.nodes.new("GeometryNodeSampleIndex")
    sample_index_008.name = "Sample Index.008"
    sample_index_008.clamp = False
    sample_index_008.data_type = 'INT'
    sample_index_008.domain = 'EDGE'

    # Node Corners of Edge.004
    corners_of_edge_004 = geometry_nodes_1.nodes.new("GeometryNodeCornersOfEdge")
    corners_of_edge_004.name = "Corners of Edge.004"
    # Edge Index
    corners_of_edge_004.inputs[0].default_value = 0
    # Weights
    corners_of_edge_004.inputs[1].default_value = 0.0
    # Sort Index
    corners_of_edge_004.inputs[2].default_value = 0

    # Node Offset Corner in Face.008
    offset_corner_in_face_008 = geometry_nodes_1.nodes.new("GeometryNodeOffsetCornerInFace")
    offset_corner_in_face_008.name = "Offset Corner in Face.008"
    # Offset
    offset_corner_in_face_008.inputs[1].default_value = 3

    # Node Offset Corner in Face.009
    offset_corner_in_face_009 = geometry_nodes_1.nodes.new("GeometryNodeOffsetCornerInFace")
    offset_corner_in_face_009.name = "Offset Corner in Face.009"
    # Offset
    offset_corner_in_face_009.inputs[1].default_value = 2

    # Node Vertex of Corner.009
    vertex_of_corner_009 = geometry_nodes_1.nodes.new("GeometryNodeVertexOfCorner")
    vertex_of_corner_009.name = "Vertex of Corner.009"
    vertex_of_corner_009.hide = True

    # Node Vertex of Corner.010
    vertex_of_corner_010 = geometry_nodes_1.nodes.new("GeometryNodeVertexOfCorner")
    vertex_of_corner_010.name = "Vertex of Corner.010"
    vertex_of_corner_010.hide = True

    # Node Compare.014
    compare_014 = geometry_nodes_1.nodes.new("FunctionNodeCompare")
    compare_014.name = "Compare.014"
    compare_014.hide = True
    compare_014.data_type = 'INT'
    compare_014.mode = 'ELEMENT'
    compare_014.operation = 'EQUAL'

    # Node Boolean Math.012
    boolean_math_012 = geometry_nodes_1.nodes.new("FunctionNodeBooleanMath")
    boolean_math_012.name = "Boolean Math.012"
    boolean_math_012.operation = 'AND'

    # Node Compare.019
    compare_019 = geometry_nodes_1.nodes.new("FunctionNodeCompare")
    compare_019.name = "Compare.019"
    compare_019.hide = True
    compare_019.data_type = 'INT'
    compare_019.mode = 'ELEMENT'
    compare_019.operation = 'EQUAL'

    # Node Edge Vertices.008
    edge_vertices_008 = geometry_nodes_1.nodes.new("GeometryNodeInputMeshEdgeVertices")
    edge_vertices_008.name = "Edge Vertices.008"

    # Node Compare.020
    compare_020 = geometry_nodes_1.nodes.new("FunctionNodeCompare")
    compare_020.name = "Compare.020"
    compare_020.hide = True
    compare_020.data_type = 'INT'
    compare_020.mode = 'ELEMENT'
    compare_020.operation = 'EQUAL'

    # Node Boolean Math.013
    boolean_math_013 = geometry_nodes_1.nodes.new("FunctionNodeBooleanMath")
    boolean_math_013.name = "Boolean Math.013"
    boolean_math_013.operation = 'AND'

    # Node Compare.021
    compare_021 = geometry_nodes_1.nodes.new("FunctionNodeCompare")
    compare_021.name = "Compare.021"
    compare_021.hide = True
    compare_021.data_type = 'INT'
    compare_021.mode = 'ELEMENT'
    compare_021.operation = 'EQUAL'

    # Node Boolean Math.014
    boolean_math_014 = geometry_nodes_1.nodes.new("FunctionNodeBooleanMath")
    boolean_math_014.name = "Boolean Math.014"
    boolean_math_014.operation = 'OR'

    # Node Sample Index.009
    sample_index_009 = geometry_nodes_1.nodes.new("GeometryNodeSampleIndex")
    sample_index_009.name = "Sample Index.009"
    sample_index_009.clamp = False
    sample_index_009.data_type = 'INT'
    sample_index_009.domain = 'EDGE'

    # Node Corners of Edge.005
    corners_of_edge_005 = geometry_nodes_1.nodes.new("GeometryNodeCornersOfEdge")
    corners_of_edge_005.name = "Corners of Edge.005"
    # Edge Index
    corners_of_edge_005.inputs[0].default_value = 0
    # Weights
    corners_of_edge_005.inputs[1].default_value = 0.0
    # Sort Index
    corners_of_edge_005.inputs[2].default_value = 1

    # Node Offset Corner in Face.010
    offset_corner_in_face_010 = geometry_nodes_1.nodes.new("GeometryNodeOffsetCornerInFace")
    offset_corner_in_face_010.name = "Offset Corner in Face.010"
    # Offset
    offset_corner_in_face_010.inputs[1].default_value = 3

    # Node Offset Corner in Face.011
    offset_corner_in_face_011 = geometry_nodes_1.nodes.new("GeometryNodeOffsetCornerInFace")
    offset_corner_in_face_011.name = "Offset Corner in Face.011"
    # Offset
    offset_corner_in_face_011.inputs[1].default_value = 2

    # Node Vertex of Corner.011
    vertex_of_corner_011 = geometry_nodes_1.nodes.new("GeometryNodeVertexOfCorner")
    vertex_of_corner_011.name = "Vertex of Corner.011"
    vertex_of_corner_011.hide = True

    # Node Vertex of Corner.012
    vertex_of_corner_012 = geometry_nodes_1.nodes.new("GeometryNodeVertexOfCorner")
    vertex_of_corner_012.name = "Vertex of Corner.012"
    vertex_of_corner_012.hide = True

    # Node Compare.022
    compare_022 = geometry_nodes_1.nodes.new("FunctionNodeCompare")
    compare_022.name = "Compare.022"
    compare_022.hide = True
    compare_022.data_type = 'INT'
    compare_022.mode = 'ELEMENT'
    compare_022.operation = 'EQUAL'

    # Node Boolean Math.015
    boolean_math_015 = geometry_nodes_1.nodes.new("FunctionNodeBooleanMath")
    boolean_math_015.name = "Boolean Math.015"
    boolean_math_015.operation = 'AND'

    # Node Compare.023
    compare_023 = geometry_nodes_1.nodes.new("FunctionNodeCompare")
    compare_023.name = "Compare.023"
    compare_023.hide = True
    compare_023.data_type = 'INT'
    compare_023.mode = 'ELEMENT'
    compare_023.operation = 'EQUAL'

    # Node Edge Vertices.009
    edge_vertices_009 = geometry_nodes_1.nodes.new("GeometryNodeInputMeshEdgeVertices")
    edge_vertices_009.name = "Edge Vertices.009"

    # Node Compare.024
    compare_024 = geometry_nodes_1.nodes.new("FunctionNodeCompare")
    compare_024.name = "Compare.024"
    compare_024.hide = True
    compare_024.data_type = 'INT'
    compare_024.mode = 'ELEMENT'
    compare_024.operation = 'EQUAL'

    # Node Boolean Math.016
    boolean_math_016 = geometry_nodes_1.nodes.new("FunctionNodeBooleanMath")
    boolean_math_016.name = "Boolean Math.016"
    boolean_math_016.operation = 'AND'

    # Node Compare.025
    compare_025 = geometry_nodes_1.nodes.new("FunctionNodeCompare")
    compare_025.name = "Compare.025"
    compare_025.hide = True
    compare_025.data_type = 'INT'
    compare_025.mode = 'ELEMENT'
    compare_025.operation = 'EQUAL'

    # Node Boolean Math.017
    boolean_math_017 = geometry_nodes_1.nodes.new("FunctionNodeBooleanMath")
    boolean_math_017.name = "Boolean Math.017"
    boolean_math_017.operation = 'OR'

    # Node Boolean Math.001
    boolean_math_001 = geometry_nodes_1.nodes.new("FunctionNodeBooleanMath")
    boolean_math_001.name = "Boolean Math.001"
    boolean_math_001.operation = 'OR'

    # Node Boolean Math.002
    boolean_math_002 = geometry_nodes_1.nodes.new("FunctionNodeBooleanMath")
    boolean_math_002.name = "Boolean Math.002"
    boolean_math_002.operation = 'OR'

    # Node Store Named Attribute
    store_named_attribute = geometry_nodes_1.nodes.new("GeometryNodeStoreNamedAttribute")
    store_named_attribute.name = "Store Named Attribute"
    store_named_attribute.data_type = 'BOOLEAN'
    store_named_attribute.domain = 'EDGE'
    # Value
    store_named_attribute.inputs[3].default_value = True

    # Node Index
    index = geometry_nodes_1.nodes.new("GeometryNodeInputIndex")
    index.name = "Index"

    # Node Compare
    compare = geometry_nodes_1.nodes.new("FunctionNodeCompare")
    compare.name = "Compare"
    compare.data_type = 'INT'
    compare.mode = 'ELEMENT'
    compare.operation = 'EQUAL'

    # Node Named Attribute.001
    named_attribute_001 = geometry_nodes_1.nodes.new("GeometryNodeInputNamedAttribute")
    named_attribute_001.name = "Named Attribute.001"
    named_attribute_001.data_type = 'BOOLEAN'
    # Name
    named_attribute_001.inputs[0].default_value = "select"

    # Node Boolean Math.018
    boolean_math_018 = geometry_nodes_1.nodes.new("FunctionNodeBooleanMath")
    boolean_math_018.name = "Boolean Math.018"
    boolean_math_018.operation = 'AND'

    # Node Named Attribute.002
    named_attribute_002 = geometry_nodes_1.nodes.new("GeometryNodeInputNamedAttribute")
    named_attribute_002.name = "Named Attribute.002"
    named_attribute_002.data_type = 'BOOLEAN'
    # Name
    named_attribute_002.inputs[0].default_value = "select"

    # Node Boolean Math.019
    boolean_math_019 = geometry_nodes_1.nodes.new("FunctionNodeBooleanMath")
    boolean_math_019.name = "Boolean Math.019"
    boolean_math_019.operation = 'NOT'

    # Node Store Named Attribute.001
    store_named_attribute_001 = geometry_nodes_1.nodes.new("GeometryNodeStoreNamedAttribute")
    store_named_attribute_001.name = "Store Named Attribute.001"
    store_named_attribute_001.data_type = 'BOOLEAN'
    store_named_attribute_001.domain = 'EDGE'
    # Name
    store_named_attribute_001.inputs[2].default_value = "select"
    # Value
    store_named_attribute_001.inputs[3].default_value = True

    # Node Compare.001
    compare_001 = geometry_nodes_1.nodes.new("FunctionNodeCompare")
    compare_001.name = "Compare.001"
    compare_001.data_type = 'INT'
    compare_001.mode = 'ELEMENT'
    compare_001.operation = 'EQUAL'

    # Node Compare.002
    compare_002 = geometry_nodes_1.nodes.new("FunctionNodeCompare")
    compare_002.name = "Compare.002"
    compare_002.data_type = 'INT'
    compare_002.mode = 'ELEMENT'
    compare_002.operation = 'EQUAL'

    # Node Boolean Math.020
    boolean_math_020 = geometry_nodes_1.nodes.new("FunctionNodeBooleanMath")
    boolean_math_020.name = "Boolean Math.020"
    boolean_math_020.operation = 'OR'

    # Node Sample Index.010
    sample_index_010 = geometry_nodes_1.nodes.new("GeometryNodeSampleIndex")
    sample_index_010.name = "Sample Index.010"
    sample_index_010.clamp = False
    sample_index_010.data_type = 'BOOLEAN'
    sample_index_010.domain = 'EDGE'

    # Node Is Edge Boundary.001
    is_edge_boundary_001 = geometry_nodes_1.nodes.new("GeometryNodeGroup")
    is_edge_boundary_001.name = "Is Edge Boundary.001"
    # Finding linked library node group
    for node_group in bpy.data.node_groups:
        if (
            node_group.name == "Is Edge Boundary"
            and node_group.bl_idname == 'GeometryNodeTree'
        ):
            is_edge_boundary_001.node_tree = node_group
    if is_edge_boundary_001.node_tree is None:
        print("Couldn't find node group Is Edge Boundary, failing")
        return

    # Node Index Switch.001
    index_switch_001 = geometry_nodes_1.nodes.new("GeometryNodeIndexSwitch")
    index_switch_001.name = "Index Switch.001"
    index_switch_001.data_type = 'INT'
    index_switch_001.index_switch_items.clear()
    index_switch_001.index_switch_items.new()
    index_switch_001.index_switch_items.new()

    # Node Sample Index.011
    sample_index_011 = geometry_nodes_1.nodes.new("GeometryNodeSampleIndex")
    sample_index_011.name = "Sample Index.011"
    sample_index_011.clamp = False
    sample_index_011.data_type = 'BOOLEAN'
    sample_index_011.domain = 'EDGE'

    # Node Is Edge Boundary.002
    is_edge_boundary_002 = geometry_nodes_1.nodes.new("GeometryNodeGroup")
    is_edge_boundary_002.name = "Is Edge Boundary.002"
    # Finding linked library node group
    for node_group in bpy.data.node_groups:
        if (
            node_group.name == "Is Edge Boundary"
            and node_group.bl_idname == 'GeometryNodeTree'
        ):
            is_edge_boundary_002.node_tree = node_group
    if is_edge_boundary_002.node_tree is None:
        print("Couldn't find node group Is Edge Boundary, failing")
        return

    # Node Index Switch.002
    index_switch_002 = geometry_nodes_1.nodes.new("GeometryNodeIndexSwitch")
    index_switch_002.name = "Index Switch.002"
    index_switch_002.data_type = 'INT'
    index_switch_002.index_switch_items.clear()
    index_switch_002.index_switch_items.new()
    index_switch_002.index_switch_items.new()

    # Node Boolean Math.021
    boolean_math_021 = geometry_nodes_1.nodes.new("FunctionNodeBooleanMath")
    boolean_math_021.name = "Boolean Math.021"
    boolean_math_021.operation = 'NOT'

    # Node Boolean Math.022
    boolean_math_022 = geometry_nodes_1.nodes.new("FunctionNodeBooleanMath")
    boolean_math_022.name = "Boolean Math.022"
    boolean_math_022.operation = 'NOT'

    # Node Repeat Input.004
    repeat_input_004 = geometry_nodes_1.nodes.new("GeometryNodeRepeatInput")
    repeat_input_004.name = "Repeat Input.004"
    # Node Repeat Output.004
    repeat_output_004 = geometry_nodes_1.nodes.new("GeometryNodeRepeatOutput")
    repeat_output_004.name = "Repeat Output.004"
    repeat_output_004.active_index = 3
    repeat_output_004.inspection_index = 0
    repeat_output_004.repeat_items.clear()
    # Create item "Geometry"
    repeat_output_004.repeat_items.new('GEOMETRY', "Geometry")
    # Create item "Integer"
    repeat_output_004.repeat_items.new('INT', "Integer")
    # Create item "Integer.001"
    repeat_output_004.repeat_items.new('INT', "Integer.001")
    # Create item "Geometry.001"
    repeat_output_004.repeat_items.new('GEOMETRY', "Geometry.001")

    # Node Is Edge Boundary.003
    is_edge_boundary_003 = geometry_nodes_1.nodes.new("GeometryNodeGroup")
    is_edge_boundary_003.name = "Is Edge Boundary.003"
    # Finding linked library node group
    for node_group in bpy.data.node_groups:
        if (
            node_group.name == "Is Edge Boundary"
            and node_group.bl_idname == 'GeometryNodeTree'
        ):
            is_edge_boundary_003.node_tree = node_group
    if is_edge_boundary_003.node_tree is None:
        print("Couldn't find node group Is Edge Boundary, failing")
        return

    # Node Named Attribute.003
    named_attribute_003 = geometry_nodes_1.nodes.new("GeometryNodeInputNamedAttribute")
    named_attribute_003.name = "Named Attribute.003"
    named_attribute_003.data_type = 'BOOLEAN'
    # Name
    named_attribute_003.inputs[0].default_value = "select"

    # Node Boolean Math.023
    boolean_math_023 = geometry_nodes_1.nodes.new("FunctionNodeBooleanMath")
    boolean_math_023.name = "Boolean Math.023"
    boolean_math_023.operation = 'AND'

    # Node Sample Index.012
    sample_index_012 = geometry_nodes_1.nodes.new("GeometryNodeSampleIndex")
    sample_index_012.name = "Sample Index.012"
    sample_index_012.clamp = False
    sample_index_012.data_type = 'BOOLEAN'
    sample_index_012.domain = 'EDGE'

    # Node Sample Index.013
    sample_index_013 = geometry_nodes_1.nodes.new("GeometryNodeSampleIndex")
    sample_index_013.name = "Sample Index.013"
    sample_index_013.clamp = False
    sample_index_013.data_type = 'BOOLEAN'
    sample_index_013.domain = 'EDGE'

    # Node Boolean Math.024
    boolean_math_024 = geometry_nodes_1.nodes.new("FunctionNodeBooleanMath")
    boolean_math_024.name = "Boolean Math.024"
    boolean_math_024.operation = 'AND'

    # Node Index Switch.003
    index_switch_003 = geometry_nodes_1.nodes.new("GeometryNodeIndexSwitch")
    index_switch_003.name = "Index Switch.003"
    index_switch_003.data_type = 'INT'
    index_switch_003.index_switch_items.clear()
    index_switch_003.index_switch_items.new()
    index_switch_003.index_switch_items.new()
    # Item_0
    index_switch_003.inputs[1].default_value = 1
    # Item_1
    index_switch_003.inputs[2].default_value = 0

    # Node String
    string = geometry_nodes_1.nodes.new("FunctionNodeInputString")
    string.name = "String"
    string.string = "select"

    # Node String.001
    string_001 = geometry_nodes_1.nodes.new("FunctionNodeInputString")
    string_001.name = "String.001"
    string_001.string = "start"

    # Node Switch
    switch = geometry_nodes_1.nodes.new("GeometryNodeSwitch")
    switch.name = "Switch"
    switch.input_type = 'STRING'

    # Node Sample Index.014
    sample_index_014 = geometry_nodes_1.nodes.new("GeometryNodeSampleIndex")
    sample_index_014.name = "Sample Index.014"
    sample_index_014.clamp = False
    sample_index_014.data_type = 'BOOLEAN'
    sample_index_014.domain = 'EDGE'

    # Node Is Edge Boundary.004
    is_edge_boundary_004 = geometry_nodes_1.nodes.new("GeometryNodeGroup")
    is_edge_boundary_004.name = "Is Edge Boundary.004"
    # Finding linked library node group
    for node_group in bpy.data.node_groups:
        if (
            node_group.name == "Is Edge Boundary"
            and node_group.bl_idname == 'GeometryNodeTree'
        ):
            is_edge_boundary_004.node_tree = node_group
    if is_edge_boundary_004.node_tree is None:
        print("Couldn't find node group Is Edge Boundary, failing")
        return

    # Node Domain Size.001
    domain_size_001 = geometry_nodes_1.nodes.new("GeometryNodeAttributeDomainSize")
    domain_size_001.name = "Domain Size.001"
    domain_size_001.component = 'MESH'

    # Node Set Material.001
    set_material_001 = geometry_nodes_1.nodes.new("GeometryNodeSetMaterial")
    set_material_001.name = "Set Material.001"
    # Selection
    set_material_001.inputs[1].default_value = True

    # Node Store Named Attribute.002
    store_named_attribute_002 = geometry_nodes_1.nodes.new("GeometryNodeStoreNamedAttribute")
    store_named_attribute_002.name = "Store Named Attribute.002"
    store_named_attribute_002.data_type = 'FLOAT_COLOR'
    store_named_attribute_002.domain = 'POINT'
    # Selection
    store_named_attribute_002.inputs[1].default_value = True
    # Name
    store_named_attribute_002.inputs[2].default_value = "Color"
    # Value
    store_named_attribute_002.inputs[3].default_value = (0.0, 0.0, 1.0, 1.0)

    # Node Store Named Attribute.003
    store_named_attribute_003 = geometry_nodes_1.nodes.new("GeometryNodeStoreNamedAttribute")
    store_named_attribute_003.name = "Store Named Attribute.003"
    store_named_attribute_003.data_type = 'FLOAT_COLOR'
    store_named_attribute_003.domain = 'POINT'
    # Selection
    store_named_attribute_003.inputs[1].default_value = True
    # Name
    store_named_attribute_003.inputs[2].default_value = "Color"
    # Value
    store_named_attribute_003.inputs[3].default_value = (1.0, 0.0, 0.0, 1.0)

    # Node UV Sphere
    uv_sphere = geometry_nodes_1.nodes.new("GeometryNodeMeshUVSphere")
    uv_sphere.name = "UV Sphere"
    # Segments
    uv_sphere.inputs[0].default_value = 32
    # Rings
    uv_sphere.inputs[1].default_value = 16
    # Radius
    uv_sphere.inputs[2].default_value = 0.05000000074505806

    # Node Set Position
    set_position = geometry_nodes_1.nodes.new("GeometryNodeSetPosition")
    set_position.name = "Set Position"
    # Selection
    set_position.inputs[1].default_value = True
    # Position
    set_position.inputs[2].default_value = (0.0, 0.0, 0.0)

    # Node Store Named Attribute.004
    store_named_attribute_004 = geometry_nodes_1.nodes.new("GeometryNodeStoreNamedAttribute")
    store_named_attribute_004.name = "Store Named Attribute.004"
    store_named_attribute_004.data_type = 'FLOAT_COLOR'
    store_named_attribute_004.domain = 'POINT'
    # Selection
    store_named_attribute_004.inputs[1].default_value = True
    # Name
    store_named_attribute_004.inputs[2].default_value = "Color"
    # Value
    store_named_attribute_004.inputs[3].default_value = (1.0, 1.0, 1.0, 1.0)

    # Process zone input Repeat Input.003
    repeat_input_003.pair_with_output(repeat_output_003)

    # Item_3
    repeat_output_003.inputs[4].default_value = 0

    # Process zone input Repeat Input.004
    repeat_input_004.pair_with_output(repeat_output_004)



    # Set locations
    geometry_nodes_1.nodes["Group Input"].location = (-1898.982421875, 697.9755859375)
    geometry_nodes_1.nodes["Group Output"].location = (5167.84912109375, 738.7174682617188)
    geometry_nodes_1.nodes["Join Geometry"].location = (4985.560546875, 735.0738525390625)
    geometry_nodes_1.nodes["Integer"].location = (-1511.082275390625, 624.560302734375)
    geometry_nodes_1.nodes["Sample Index.003"].location = (1123.3541259765625, -603.870849609375)
    geometry_nodes_1.nodes["Edge Vertices"].location = (433.127685546875, -774.4301147460938)
    geometry_nodes_1.nodes["Vector Math"].location = (672.11376953125, -774.2687377929688)
    geometry_nodes_1.nodes["Vector Math.001"].location = (866.1678466796875, -824.0400390625)
    geometry_nodes_1.nodes["Mesh to Curve"].location = (4148.62646484375, 530.8082885742188)
    geometry_nodes_1.nodes["Curve to Tube"].location = (4334.91064453125, 488.96307373046875)
    geometry_nodes_1.nodes["Set Material"].location = (4591.15380859375, 452.5946350097656)
    geometry_nodes_1.nodes["Repeat Input.003"].location = (-79.75843811035156, 504.9410095214844)
    geometry_nodes_1.nodes["Repeat Output.003"].location = (3455.055908203125, 453.3616638183594)
    geometry_nodes_1.nodes["Sample Index.006"].location = (627.2523803710938, 806.1484375)
    geometry_nodes_1.nodes["Corners of Edge.002"].location = (451.9744567871094, 821.13232421875)
    geometry_nodes_1.nodes["Offset Corner in Face.004"].location = (804.9964599609375, 709.2232666015625)
    geometry_nodes_1.nodes["Offset Corner in Face.005"].location = (805.9574584960938, 828.82177734375)
    geometry_nodes_1.nodes["Vertex of Corner.005"].location = (985.9283447265625, 879.5491943359375)
    geometry_nodes_1.nodes["Vertex of Corner.006"].location = (984.4474487304688, 704.7298583984375)
    geometry_nodes_1.nodes["Compare.010"].location = (1217.162353515625, 764.9151611328125)
    geometry_nodes_1.nodes["Boolean Math.006"].location = (1410.328125, 787.4742431640625)
    geometry_nodes_1.nodes["Compare.011"].location = (1217.3857421875, 710.817626953125)
    geometry_nodes_1.nodes["Edge Vertices.006"].location = (990.6419677734375, 839.957275390625)
    geometry_nodes_1.nodes["Compare.012"].location = (1218.140869140625, 887.6356201171875)
    geometry_nodes_1.nodes["Boolean Math.007"].location = (1409.657470703125, 923.6007080078125)
    geometry_nodes_1.nodes["Compare.013"].location = (1215.59765625, 827.9969482421875)
    geometry_nodes_1.nodes["Boolean Math.008"].location = (1607.06494140625, 873.6904296875)
    geometry_nodes_1.nodes["Attribute Statistic.001"].location = (2475.82177734375, 880.1738891601562)
    geometry_nodes_1.nodes["Index.003"].location = (2492.72265625, 532.2880249023438)
    geometry_nodes_1.nodes["Duplicate Elements.001"].location = (2203.412109375, 259.3551940917969)
    geometry_nodes_1.nodes["Set Position.001"].location = (2368.588134765625, 311.381591796875)
    geometry_nodes_1.nodes["Join Geometry.003"].location = (2527.661865234375, 376.4574279785156)
    geometry_nodes_1.nodes["Sample Index.007"].location = (636.9526977539062, 529.2745361328125)
    geometry_nodes_1.nodes["Corners of Edge.003"].location = (461.6747741699219, 544.2584228515625)
    geometry_nodes_1.nodes["Offset Corner in Face.006"].location = (814.69677734375, 432.3494567871094)
    geometry_nodes_1.nodes["Offset Corner in Face.007"].location = (815.6577758789062, 551.947998046875)
    geometry_nodes_1.nodes["Vertex of Corner.007"].location = (995.628662109375, 602.67529296875)
    geometry_nodes_1.nodes["Vertex of Corner.008"].location = (994.1477661132812, 427.8560485839844)
    geometry_nodes_1.nodes["Compare.015"].location = (1226.86279296875, 488.0413513183594)
    geometry_nodes_1.nodes["Boolean Math.009"].location = (1420.028564453125, 510.6004333496094)
    geometry_nodes_1.nodes["Compare.016"].location = (1227.086181640625, 433.9438171386719)
    geometry_nodes_1.nodes["Edge Vertices.007"].location = (1000.34228515625, 563.08349609375)
    geometry_nodes_1.nodes["Compare.017"].location = (1227.841064453125, 610.7618408203125)
    geometry_nodes_1.nodes["Boolean Math.010"].location = (1419.35791015625, 646.726806640625)
    geometry_nodes_1.nodes["Compare.018"].location = (1225.298095703125, 551.123046875)
    geometry_nodes_1.nodes["Boolean Math.011"].location = (1616.76513671875, 596.8165283203125)
    geometry_nodes_1.nodes["Boolean Math"].location = (1816.292724609375, 722.915283203125)
    geometry_nodes_1.nodes["Sample Index.008"].location = (653.4221801757812, 191.28134155273438)
    geometry_nodes_1.nodes["Corners of Edge.004"].location = (478.144287109375, 206.26522827148438)
    geometry_nodes_1.nodes["Offset Corner in Face.008"].location = (831.166259765625, 94.35623168945312)
    geometry_nodes_1.nodes["Offset Corner in Face.009"].location = (832.1272583007812, 213.95474243164062)
    geometry_nodes_1.nodes["Vertex of Corner.009"].location = (1012.09814453125, 264.6820983886719)
    geometry_nodes_1.nodes["Vertex of Corner.010"].location = (1010.6173095703125, 89.86282348632812)
    geometry_nodes_1.nodes["Compare.014"].location = (1243.332275390625, 150.04812622070312)
    geometry_nodes_1.nodes["Boolean Math.012"].location = (1436.498046875, 172.60720825195312)
    geometry_nodes_1.nodes["Compare.019"].location = (1243.5556640625, 95.95059204101562)
    geometry_nodes_1.nodes["Edge Vertices.008"].location = (1016.811767578125, 225.09024047851562)
    geometry_nodes_1.nodes["Compare.020"].location = (1244.3106689453125, 272.7685852050781)
    geometry_nodes_1.nodes["Boolean Math.013"].location = (1435.827392578125, 308.7336120605469)
    geometry_nodes_1.nodes["Compare.021"].location = (1241.767578125, 213.12985229492188)
    geometry_nodes_1.nodes["Boolean Math.014"].location = (1633.2347412109375, 258.8233337402344)
    geometry_nodes_1.nodes["Sample Index.009"].location = (663.1224975585938, -85.59249877929688)
    geometry_nodes_1.nodes["Corners of Edge.005"].location = (487.8446044921875, -70.60861206054688)
    geometry_nodes_1.nodes["Offset Corner in Face.010"].location = (840.8665771484375, -182.51760864257812)
    geometry_nodes_1.nodes["Offset Corner in Face.011"].location = (841.8275756835938, -62.919097900390625)
    geometry_nodes_1.nodes["Vertex of Corner.011"].location = (1021.7984619140625, -12.191741943359375)
    geometry_nodes_1.nodes["Vertex of Corner.012"].location = (1020.3175048828125, -187.01101684570312)
    geometry_nodes_1.nodes["Compare.022"].location = (1253.0325927734375, -126.82571411132812)
    geometry_nodes_1.nodes["Boolean Math.015"].location = (1446.1983642578125, -104.26663208007812)
    geometry_nodes_1.nodes["Compare.023"].location = (1253.2559814453125, -180.92324829101562)
    geometry_nodes_1.nodes["Edge Vertices.009"].location = (1026.5120849609375, -51.783599853515625)
    geometry_nodes_1.nodes["Compare.024"].location = (1254.010986328125, -4.105255126953125)
    geometry_nodes_1.nodes["Boolean Math.016"].location = (1445.5277099609375, 31.859771728515625)
    geometry_nodes_1.nodes["Compare.025"].location = (1251.4678955078125, -63.743988037109375)
    geometry_nodes_1.nodes["Boolean Math.017"].location = (1642.93505859375, -18.050506591796875)
    geometry_nodes_1.nodes["Boolean Math.001"].location = (1842.4625244140625, 108.04818725585938)
    geometry_nodes_1.nodes["Boolean Math.002"].location = (1999.5115966796875, 294.49517822265625)
    geometry_nodes_1.nodes["Store Named Attribute"].location = (-879.6141967773438, 940.1071166992188)
    geometry_nodes_1.nodes["Index"].location = (-1282.09521484375, 688.3594360351562)
    geometry_nodes_1.nodes["Compare"].location = (-1094.7613525390625, 755.8142700195312)
    geometry_nodes_1.nodes["Named Attribute.001"].location = (4098.98291015625, 333.0413818359375)
    geometry_nodes_1.nodes["Boolean Math.018"].location = (2307.7041015625, 593.8483276367188)
    geometry_nodes_1.nodes["Named Attribute.002"].location = (2085.191162109375, 778.389404296875)
    geometry_nodes_1.nodes["Boolean Math.019"].location = (2258.0068359375, 780.7603149414062)
    geometry_nodes_1.nodes["Store Named Attribute.001"].location = (3157.212158203125, 659.5773315429688)
    geometry_nodes_1.nodes["Compare.001"].location = (2771.48046875, 520.1793212890625)
    geometry_nodes_1.nodes["Compare.002"].location = (2771.48046875, 330.5081481933594)
    geometry_nodes_1.nodes["Boolean Math.020"].location = (2979.560546875, 314.7682800292969)
    geometry_nodes_1.nodes["Sample Index.010"].location = (3078.201904296875, 993.2219848632812)
    geometry_nodes_1.nodes["Is Edge Boundary.001"].location = (2629.761474609375, 1025.709228515625)
    geometry_nodes_1.nodes["Index Switch.001"].location = (3258.606201171875, 868.7927856445312)
    geometry_nodes_1.nodes["Sample Index.011"].location = (3031.132080078125, 1319.5931396484375)
    geometry_nodes_1.nodes["Is Edge Boundary.002"].location = (2678.89306640625, 1215.6787109375)
    geometry_nodes_1.nodes["Index Switch.002"].location = (3285.133544921875, 1201.4241943359375)
    geometry_nodes_1.nodes["Boolean Math.021"].location = (2845.881103515625, 1300.368896484375)
    geometry_nodes_1.nodes["Boolean Math.022"].location = (2867.16845703125, 997.238037109375)
    geometry_nodes_1.nodes["Repeat Input.004"].location = (-635.4944458007812, 685.1001586914062)
    geometry_nodes_1.nodes["Repeat Output.004"].location = (3946.132568359375, 640.0020751953125)
    geometry_nodes_1.nodes["Is Edge Boundary.003"].location = (-572.5744018554688, 907.2012939453125)
    geometry_nodes_1.nodes["Named Attribute.003"].location = (-573.010986328125, 839.0078735351562)
    geometry_nodes_1.nodes["Boolean Math.023"].location = (-409.7601318359375, 947.081298828125)
    geometry_nodes_1.nodes["Sample Index.012"].location = (-224.37364196777344, 1019.1302490234375)
    geometry_nodes_1.nodes["Sample Index.013"].location = (-216.07275390625, 794.6701049804688)
    geometry_nodes_1.nodes["Boolean Math.024"].location = (-22.3765869140625, 961.1549682617188)
    geometry_nodes_1.nodes["Index Switch.003"].location = (155.7172088623047, 988.0938110351562)
    geometry_nodes_1.nodes["String"].location = (-1086.5760498046875, 1032.673095703125)
    geometry_nodes_1.nodes["String.001"].location = (-1088.943359375, 961.5419311523438)
    geometry_nodes_1.nodes["Switch"].location = (-888.9339599609375, 1165.2042236328125)
    geometry_nodes_1.nodes["Sample Index.014"].location = (-1217.67236328125, 1207.103759765625)
    geometry_nodes_1.nodes["Is Edge Boundary.004"].location = (-1404.5506591796875, 1187.8135986328125)
    geometry_nodes_1.nodes["Domain Size.001"].location = (-846.147216796875, 535.4356079101562)
    geometry_nodes_1.nodes["Set Material.001"].location = (4602.6298828125, 127.25546264648438)
    geometry_nodes_1.nodes["Store Named Attribute.002"].location = (4780.97216796875, 303.3134765625)
    geometry_nodes_1.nodes["Store Named Attribute.003"].location = (4776.39892578125, 534.4163818359375)
    geometry_nodes_1.nodes["UV Sphere"].location = (3798.54345703125, -350.01434326171875)
    geometry_nodes_1.nodes["Set Position"].location = (4080.328857421875, -187.95079040527344)
    geometry_nodes_1.nodes["Store Named Attribute.004"].location = (4764.4228515625, 763.739013671875)

    # Set dimensions
    geometry_nodes_1.nodes["Group Input"].width  = 140.0
    geometry_nodes_1.nodes["Group Input"].height = 100.0

    geometry_nodes_1.nodes["Group Output"].width  = 152.796875
    geometry_nodes_1.nodes["Group Output"].height = 100.0

    geometry_nodes_1.nodes["Join Geometry"].width  = 140.0
    geometry_nodes_1.nodes["Join Geometry"].height = 100.0

    geometry_nodes_1.nodes["Integer"].width  = 140.0
    geometry_nodes_1.nodes["Integer"].height = 100.0

    geometry_nodes_1.nodes["Sample Index.003"].width  = 140.0
    geometry_nodes_1.nodes["Sample Index.003"].height = 100.0

    geometry_nodes_1.nodes["Edge Vertices"].width  = 140.0
    geometry_nodes_1.nodes["Edge Vertices"].height = 100.0

    geometry_nodes_1.nodes["Vector Math"].width  = 140.0
    geometry_nodes_1.nodes["Vector Math"].height = 100.0

    geometry_nodes_1.nodes["Vector Math.001"].width  = 140.0
    geometry_nodes_1.nodes["Vector Math.001"].height = 100.0

    geometry_nodes_1.nodes["Mesh to Curve"].width  = 140.0
    geometry_nodes_1.nodes["Mesh to Curve"].height = 100.0

    geometry_nodes_1.nodes["Curve to Tube"].width  = 200.0
    geometry_nodes_1.nodes["Curve to Tube"].height = 100.0

    geometry_nodes_1.nodes["Set Material"].width  = 140.0
    geometry_nodes_1.nodes["Set Material"].height = 100.0

    geometry_nodes_1.nodes["Repeat Input.003"].width  = 140.0
    geometry_nodes_1.nodes["Repeat Input.003"].height = 100.0

    geometry_nodes_1.nodes["Repeat Output.003"].width  = 140.0
    geometry_nodes_1.nodes["Repeat Output.003"].height = 100.0

    geometry_nodes_1.nodes["Sample Index.006"].width  = 140.0
    geometry_nodes_1.nodes["Sample Index.006"].height = 100.0

    geometry_nodes_1.nodes["Corners of Edge.002"].width  = 140.0
    geometry_nodes_1.nodes["Corners of Edge.002"].height = 100.0

    geometry_nodes_1.nodes["Offset Corner in Face.004"].width  = 150.84442138671875
    geometry_nodes_1.nodes["Offset Corner in Face.004"].height = 100.0

    geometry_nodes_1.nodes["Offset Corner in Face.005"].width  = 147.00537109375
    geometry_nodes_1.nodes["Offset Corner in Face.005"].height = 100.0

    geometry_nodes_1.nodes["Vertex of Corner.005"].width  = 140.0
    geometry_nodes_1.nodes["Vertex of Corner.005"].height = 100.0

    geometry_nodes_1.nodes["Vertex of Corner.006"].width  = 156.1668701171875
    geometry_nodes_1.nodes["Vertex of Corner.006"].height = 100.0

    geometry_nodes_1.nodes["Compare.010"].width  = 140.0
    geometry_nodes_1.nodes["Compare.010"].height = 100.0

    geometry_nodes_1.nodes["Boolean Math.006"].width  = 140.0
    geometry_nodes_1.nodes["Boolean Math.006"].height = 100.0

    geometry_nodes_1.nodes["Compare.011"].width  = 140.0
    geometry_nodes_1.nodes["Compare.011"].height = 100.0

    geometry_nodes_1.nodes["Edge Vertices.006"].width  = 140.0
    geometry_nodes_1.nodes["Edge Vertices.006"].height = 100.0

    geometry_nodes_1.nodes["Compare.012"].width  = 140.0
    geometry_nodes_1.nodes["Compare.012"].height = 100.0

    geometry_nodes_1.nodes["Boolean Math.007"].width  = 140.0
    geometry_nodes_1.nodes["Boolean Math.007"].height = 100.0

    geometry_nodes_1.nodes["Compare.013"].width  = 140.0
    geometry_nodes_1.nodes["Compare.013"].height = 100.0

    geometry_nodes_1.nodes["Boolean Math.008"].width  = 140.0
    geometry_nodes_1.nodes["Boolean Math.008"].height = 100.0

    geometry_nodes_1.nodes["Attribute Statistic.001"].width  = 140.0
    geometry_nodes_1.nodes["Attribute Statistic.001"].height = 100.0

    geometry_nodes_1.nodes["Index.003"].width  = 140.0
    geometry_nodes_1.nodes["Index.003"].height = 100.0

    geometry_nodes_1.nodes["Duplicate Elements.001"].width  = 140.0
    geometry_nodes_1.nodes["Duplicate Elements.001"].height = 100.0

    geometry_nodes_1.nodes["Set Position.001"].width  = 140.0
    geometry_nodes_1.nodes["Set Position.001"].height = 100.0

    geometry_nodes_1.nodes["Join Geometry.003"].width  = 140.0
    geometry_nodes_1.nodes["Join Geometry.003"].height = 100.0

    geometry_nodes_1.nodes["Sample Index.007"].width  = 140.0
    geometry_nodes_1.nodes["Sample Index.007"].height = 100.0

    geometry_nodes_1.nodes["Corners of Edge.003"].width  = 140.0
    geometry_nodes_1.nodes["Corners of Edge.003"].height = 100.0

    geometry_nodes_1.nodes["Offset Corner in Face.006"].width  = 150.84442138671875
    geometry_nodes_1.nodes["Offset Corner in Face.006"].height = 100.0

    geometry_nodes_1.nodes["Offset Corner in Face.007"].width  = 147.00537109375
    geometry_nodes_1.nodes["Offset Corner in Face.007"].height = 100.0

    geometry_nodes_1.nodes["Vertex of Corner.007"].width  = 140.0
    geometry_nodes_1.nodes["Vertex of Corner.007"].height = 100.0

    geometry_nodes_1.nodes["Vertex of Corner.008"].width  = 156.1668701171875
    geometry_nodes_1.nodes["Vertex of Corner.008"].height = 100.0

    geometry_nodes_1.nodes["Compare.015"].width  = 140.0
    geometry_nodes_1.nodes["Compare.015"].height = 100.0

    geometry_nodes_1.nodes["Boolean Math.009"].width  = 140.0
    geometry_nodes_1.nodes["Boolean Math.009"].height = 100.0

    geometry_nodes_1.nodes["Compare.016"].width  = 140.0
    geometry_nodes_1.nodes["Compare.016"].height = 100.0

    geometry_nodes_1.nodes["Edge Vertices.007"].width  = 140.0
    geometry_nodes_1.nodes["Edge Vertices.007"].height = 100.0

    geometry_nodes_1.nodes["Compare.017"].width  = 140.0
    geometry_nodes_1.nodes["Compare.017"].height = 100.0

    geometry_nodes_1.nodes["Boolean Math.010"].width  = 140.0
    geometry_nodes_1.nodes["Boolean Math.010"].height = 100.0

    geometry_nodes_1.nodes["Compare.018"].width  = 140.0
    geometry_nodes_1.nodes["Compare.018"].height = 100.0

    geometry_nodes_1.nodes["Boolean Math.011"].width  = 140.0
    geometry_nodes_1.nodes["Boolean Math.011"].height = 100.0

    geometry_nodes_1.nodes["Boolean Math"].width  = 140.0
    geometry_nodes_1.nodes["Boolean Math"].height = 100.0

    geometry_nodes_1.nodes["Sample Index.008"].width  = 140.0
    geometry_nodes_1.nodes["Sample Index.008"].height = 100.0

    geometry_nodes_1.nodes["Corners of Edge.004"].width  = 140.0
    geometry_nodes_1.nodes["Corners of Edge.004"].height = 100.0

    geometry_nodes_1.nodes["Offset Corner in Face.008"].width  = 150.84442138671875
    geometry_nodes_1.nodes["Offset Corner in Face.008"].height = 100.0

    geometry_nodes_1.nodes["Offset Corner in Face.009"].width  = 147.00537109375
    geometry_nodes_1.nodes["Offset Corner in Face.009"].height = 100.0

    geometry_nodes_1.nodes["Vertex of Corner.009"].width  = 140.0
    geometry_nodes_1.nodes["Vertex of Corner.009"].height = 100.0

    geometry_nodes_1.nodes["Vertex of Corner.010"].width  = 156.1668701171875
    geometry_nodes_1.nodes["Vertex of Corner.010"].height = 100.0

    geometry_nodes_1.nodes["Compare.014"].width  = 140.0
    geometry_nodes_1.nodes["Compare.014"].height = 100.0

    geometry_nodes_1.nodes["Boolean Math.012"].width  = 140.0
    geometry_nodes_1.nodes["Boolean Math.012"].height = 100.0

    geometry_nodes_1.nodes["Compare.019"].width  = 140.0
    geometry_nodes_1.nodes["Compare.019"].height = 100.0

    geometry_nodes_1.nodes["Edge Vertices.008"].width  = 140.0
    geometry_nodes_1.nodes["Edge Vertices.008"].height = 100.0

    geometry_nodes_1.nodes["Compare.020"].width  = 140.0
    geometry_nodes_1.nodes["Compare.020"].height = 100.0

    geometry_nodes_1.nodes["Boolean Math.013"].width  = 140.0
    geometry_nodes_1.nodes["Boolean Math.013"].height = 100.0

    geometry_nodes_1.nodes["Compare.021"].width  = 140.0
    geometry_nodes_1.nodes["Compare.021"].height = 100.0

    geometry_nodes_1.nodes["Boolean Math.014"].width  = 140.0
    geometry_nodes_1.nodes["Boolean Math.014"].height = 100.0

    geometry_nodes_1.nodes["Sample Index.009"].width  = 140.0
    geometry_nodes_1.nodes["Sample Index.009"].height = 100.0

    geometry_nodes_1.nodes["Corners of Edge.005"].width  = 140.0
    geometry_nodes_1.nodes["Corners of Edge.005"].height = 100.0

    geometry_nodes_1.nodes["Offset Corner in Face.010"].width  = 150.84442138671875
    geometry_nodes_1.nodes["Offset Corner in Face.010"].height = 100.0

    geometry_nodes_1.nodes["Offset Corner in Face.011"].width  = 147.00537109375
    geometry_nodes_1.nodes["Offset Corner in Face.011"].height = 100.0

    geometry_nodes_1.nodes["Vertex of Corner.011"].width  = 140.0
    geometry_nodes_1.nodes["Vertex of Corner.011"].height = 100.0

    geometry_nodes_1.nodes["Vertex of Corner.012"].width  = 156.1668701171875
    geometry_nodes_1.nodes["Vertex of Corner.012"].height = 100.0

    geometry_nodes_1.nodes["Compare.022"].width  = 140.0
    geometry_nodes_1.nodes["Compare.022"].height = 100.0

    geometry_nodes_1.nodes["Boolean Math.015"].width  = 140.0
    geometry_nodes_1.nodes["Boolean Math.015"].height = 100.0

    geometry_nodes_1.nodes["Compare.023"].width  = 140.0
    geometry_nodes_1.nodes["Compare.023"].height = 100.0

    geometry_nodes_1.nodes["Edge Vertices.009"].width  = 140.0
    geometry_nodes_1.nodes["Edge Vertices.009"].height = 100.0

    geometry_nodes_1.nodes["Compare.024"].width  = 140.0
    geometry_nodes_1.nodes["Compare.024"].height = 100.0

    geometry_nodes_1.nodes["Boolean Math.016"].width  = 140.0
    geometry_nodes_1.nodes["Boolean Math.016"].height = 100.0

    geometry_nodes_1.nodes["Compare.025"].width  = 140.0
    geometry_nodes_1.nodes["Compare.025"].height = 100.0

    geometry_nodes_1.nodes["Boolean Math.017"].width  = 140.0
    geometry_nodes_1.nodes["Boolean Math.017"].height = 100.0

    geometry_nodes_1.nodes["Boolean Math.001"].width  = 140.0
    geometry_nodes_1.nodes["Boolean Math.001"].height = 100.0

    geometry_nodes_1.nodes["Boolean Math.002"].width  = 140.0
    geometry_nodes_1.nodes["Boolean Math.002"].height = 100.0

    geometry_nodes_1.nodes["Store Named Attribute"].width  = 140.0
    geometry_nodes_1.nodes["Store Named Attribute"].height = 100.0

    geometry_nodes_1.nodes["Index"].width  = 140.0
    geometry_nodes_1.nodes["Index"].height = 100.0

    geometry_nodes_1.nodes["Compare"].width  = 140.0
    geometry_nodes_1.nodes["Compare"].height = 100.0

    geometry_nodes_1.nodes["Named Attribute.001"].width  = 140.0
    geometry_nodes_1.nodes["Named Attribute.001"].height = 100.0

    geometry_nodes_1.nodes["Boolean Math.018"].width  = 140.0
    geometry_nodes_1.nodes["Boolean Math.018"].height = 100.0

    geometry_nodes_1.nodes["Named Attribute.002"].width  = 140.0
    geometry_nodes_1.nodes["Named Attribute.002"].height = 100.0

    geometry_nodes_1.nodes["Boolean Math.019"].width  = 140.0
    geometry_nodes_1.nodes["Boolean Math.019"].height = 100.0

    geometry_nodes_1.nodes["Store Named Attribute.001"].width  = 140.0
    geometry_nodes_1.nodes["Store Named Attribute.001"].height = 100.0

    geometry_nodes_1.nodes["Compare.001"].width  = 140.0
    geometry_nodes_1.nodes["Compare.001"].height = 100.0

    geometry_nodes_1.nodes["Compare.002"].width  = 140.0
    geometry_nodes_1.nodes["Compare.002"].height = 100.0

    geometry_nodes_1.nodes["Boolean Math.020"].width  = 140.0
    geometry_nodes_1.nodes["Boolean Math.020"].height = 100.0

    geometry_nodes_1.nodes["Sample Index.010"].width  = 140.0
    geometry_nodes_1.nodes["Sample Index.010"].height = 100.0

    geometry_nodes_1.nodes["Is Edge Boundary.001"].width  = 140.0
    geometry_nodes_1.nodes["Is Edge Boundary.001"].height = 100.0

    geometry_nodes_1.nodes["Index Switch.001"].width  = 140.0
    geometry_nodes_1.nodes["Index Switch.001"].height = 100.0

    geometry_nodes_1.nodes["Sample Index.011"].width  = 140.0
    geometry_nodes_1.nodes["Sample Index.011"].height = 100.0

    geometry_nodes_1.nodes["Is Edge Boundary.002"].width  = 140.0
    geometry_nodes_1.nodes["Is Edge Boundary.002"].height = 100.0

    geometry_nodes_1.nodes["Index Switch.002"].width  = 140.0
    geometry_nodes_1.nodes["Index Switch.002"].height = 100.0

    geometry_nodes_1.nodes["Boolean Math.021"].width  = 140.0
    geometry_nodes_1.nodes["Boolean Math.021"].height = 100.0

    geometry_nodes_1.nodes["Boolean Math.022"].width  = 140.0
    geometry_nodes_1.nodes["Boolean Math.022"].height = 100.0

    geometry_nodes_1.nodes["Repeat Input.004"].width  = 140.0
    geometry_nodes_1.nodes["Repeat Input.004"].height = 100.0

    geometry_nodes_1.nodes["Repeat Output.004"].width  = 140.0
    geometry_nodes_1.nodes["Repeat Output.004"].height = 100.0

    geometry_nodes_1.nodes["Is Edge Boundary.003"].width  = 140.0
    geometry_nodes_1.nodes["Is Edge Boundary.003"].height = 100.0

    geometry_nodes_1.nodes["Named Attribute.003"].width  = 140.0
    geometry_nodes_1.nodes["Named Attribute.003"].height = 100.0

    geometry_nodes_1.nodes["Boolean Math.023"].width  = 140.0
    geometry_nodes_1.nodes["Boolean Math.023"].height = 100.0

    geometry_nodes_1.nodes["Sample Index.012"].width  = 140.0
    geometry_nodes_1.nodes["Sample Index.012"].height = 100.0

    geometry_nodes_1.nodes["Sample Index.013"].width  = 140.0
    geometry_nodes_1.nodes["Sample Index.013"].height = 100.0

    geometry_nodes_1.nodes["Boolean Math.024"].width  = 140.0
    geometry_nodes_1.nodes["Boolean Math.024"].height = 100.0

    geometry_nodes_1.nodes["Index Switch.003"].width  = 140.0
    geometry_nodes_1.nodes["Index Switch.003"].height = 100.0

    geometry_nodes_1.nodes["String"].width  = 140.0
    geometry_nodes_1.nodes["String"].height = 100.0

    geometry_nodes_1.nodes["String.001"].width  = 140.0
    geometry_nodes_1.nodes["String.001"].height = 100.0

    geometry_nodes_1.nodes["Switch"].width  = 140.0
    geometry_nodes_1.nodes["Switch"].height = 100.0

    geometry_nodes_1.nodes["Sample Index.014"].width  = 140.0
    geometry_nodes_1.nodes["Sample Index.014"].height = 100.0

    geometry_nodes_1.nodes["Is Edge Boundary.004"].width  = 140.0
    geometry_nodes_1.nodes["Is Edge Boundary.004"].height = 100.0

    geometry_nodes_1.nodes["Domain Size.001"].width  = 140.0
    geometry_nodes_1.nodes["Domain Size.001"].height = 100.0

    geometry_nodes_1.nodes["Set Material.001"].width  = 140.0
    geometry_nodes_1.nodes["Set Material.001"].height = 100.0

    geometry_nodes_1.nodes["Store Named Attribute.002"].width  = 140.0
    geometry_nodes_1.nodes["Store Named Attribute.002"].height = 100.0

    geometry_nodes_1.nodes["Store Named Attribute.003"].width  = 140.0
    geometry_nodes_1.nodes["Store Named Attribute.003"].height = 100.0

    geometry_nodes_1.nodes["UV Sphere"].width  = 140.0
    geometry_nodes_1.nodes["UV Sphere"].height = 100.0

    geometry_nodes_1.nodes["Set Position"].width  = 140.0
    geometry_nodes_1.nodes["Set Position"].height = 100.0

    geometry_nodes_1.nodes["Store Named Attribute.004"].width  = 140.0
    geometry_nodes_1.nodes["Store Named Attribute.004"].height = 100.0


    # Initialize geometry_nodes_1 links

    # group_input.Geometry -> sample_index_003.Geometry
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Group Input"].outputs[0],
        geometry_nodes_1.nodes["Sample Index.003"].inputs[0]
    )
    # edge_vertices.Position 1 -> vector_math.Vector
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Edge Vertices"].outputs[2],
        geometry_nodes_1.nodes["Vector Math"].inputs[0]
    )
    # edge_vertices.Position 2 -> vector_math.Vector
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Edge Vertices"].outputs[3],
        geometry_nodes_1.nodes["Vector Math"].inputs[1]
    )
    # vector_math.Vector -> vector_math_001.Vector
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Vector Math"].outputs[0],
        geometry_nodes_1.nodes["Vector Math.001"].inputs[0]
    )
    # vector_math_001.Vector -> sample_index_003.Value
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Vector Math.001"].outputs[0],
        geometry_nodes_1.nodes["Sample Index.003"].inputs[1]
    )
    # integer.Integer -> sample_index_003.Index
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Integer"].outputs[0],
        geometry_nodes_1.nodes["Sample Index.003"].inputs[2]
    )
    # mesh_to_curve.Curve -> curve_to_tube.Curve
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Mesh to Curve"].outputs[0],
        geometry_nodes_1.nodes["Curve to Tube"].inputs[0]
    )
    # curve_to_tube.Mesh -> set_material.Geometry
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Curve to Tube"].outputs[0],
        geometry_nodes_1.nodes["Set Material"].inputs[0]
    )
    # corners_of_edge_002.Corner Index -> sample_index_006.Value
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Corners of Edge.002"].outputs[0],
        geometry_nodes_1.nodes["Sample Index.006"].inputs[1]
    )
    # sample_index_006.Value -> offset_corner_in_face_004.Corner Index
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Sample Index.006"].outputs[0],
        geometry_nodes_1.nodes["Offset Corner in Face.004"].inputs[0]
    )
    # sample_index_006.Value -> offset_corner_in_face_005.Corner Index
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Sample Index.006"].outputs[0],
        geometry_nodes_1.nodes["Offset Corner in Face.005"].inputs[0]
    )
    # offset_corner_in_face_005.Corner Index -> vertex_of_corner_005.Corner Index
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Offset Corner in Face.005"].outputs[0],
        geometry_nodes_1.nodes["Vertex of Corner.005"].inputs[0]
    )
    # offset_corner_in_face_004.Corner Index -> vertex_of_corner_006.Corner Index
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Offset Corner in Face.004"].outputs[0],
        geometry_nodes_1.nodes["Vertex of Corner.006"].inputs[0]
    )
    # vertex_of_corner_005.Vertex Index -> compare_010.B
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Vertex of Corner.005"].outputs[0],
        geometry_nodes_1.nodes["Compare.010"].inputs[3]
    )
    # compare_010.Result -> boolean_math_006.Boolean
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Compare.010"].outputs[0],
        geometry_nodes_1.nodes["Boolean Math.006"].inputs[0]
    )
    # vertex_of_corner_006.Vertex Index -> compare_011.B
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Vertex of Corner.006"].outputs[0],
        geometry_nodes_1.nodes["Compare.011"].inputs[3]
    )
    # compare_011.Result -> boolean_math_006.Boolean
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Compare.011"].outputs[0],
        geometry_nodes_1.nodes["Boolean Math.006"].inputs[1]
    )
    # compare_012.Result -> boolean_math_007.Boolean
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Compare.012"].outputs[0],
        geometry_nodes_1.nodes["Boolean Math.007"].inputs[0]
    )
    # compare_013.Result -> boolean_math_007.Boolean
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Compare.013"].outputs[0],
        geometry_nodes_1.nodes["Boolean Math.007"].inputs[1]
    )
    # vertex_of_corner_005.Vertex Index -> compare_012.B
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Vertex of Corner.005"].outputs[0],
        geometry_nodes_1.nodes["Compare.012"].inputs[3]
    )
    # vertex_of_corner_006.Vertex Index -> compare_013.B
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Vertex of Corner.006"].outputs[0],
        geometry_nodes_1.nodes["Compare.013"].inputs[3]
    )
    # edge_vertices_006.Vertex Index 2 -> compare_012.A
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Edge Vertices.006"].outputs[1],
        geometry_nodes_1.nodes["Compare.012"].inputs[2]
    )
    # edge_vertices_006.Vertex Index 1 -> compare_013.A
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Edge Vertices.006"].outputs[0],
        geometry_nodes_1.nodes["Compare.013"].inputs[2]
    )
    # boolean_math_007.Boolean -> boolean_math_008.Boolean
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Boolean Math.007"].outputs[0],
        geometry_nodes_1.nodes["Boolean Math.008"].inputs[0]
    )
    # boolean_math_006.Boolean -> boolean_math_008.Boolean
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Boolean Math.006"].outputs[0],
        geometry_nodes_1.nodes["Boolean Math.008"].inputs[1]
    )
    # repeat_input_003.Geometry -> sample_index_006.Geometry
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Repeat Input.003"].outputs[1],
        geometry_nodes_1.nodes["Sample Index.006"].inputs[0]
    )
    # repeat_input_003.Geometry -> attribute_statistic_001.Geometry
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Repeat Input.003"].outputs[1],
        geometry_nodes_1.nodes["Attribute Statistic.001"].inputs[0]
    )
    # repeat_input_003.Geometry -> duplicate_elements_001.Geometry
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Repeat Input.003"].outputs[1],
        geometry_nodes_1.nodes["Duplicate Elements.001"].inputs[0]
    )
    # duplicate_elements_001.Geometry -> set_position_001.Geometry
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Duplicate Elements.001"].outputs[0],
        geometry_nodes_1.nodes["Set Position.001"].inputs[0]
    )
    # store_named_attribute_001.Geometry -> repeat_output_003.Geometry
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Store Named Attribute.001"].outputs[0],
        geometry_nodes_1.nodes["Repeat Output.003"].inputs[0]
    )
    # set_position_001.Geometry -> join_geometry_003.Geometry
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Set Position.001"].outputs[0],
        geometry_nodes_1.nodes["Join Geometry.003"].inputs[0]
    )
    # join_geometry_003.Geometry -> repeat_output_003.Geometry.001
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Join Geometry.003"].outputs[0],
        geometry_nodes_1.nodes["Repeat Output.003"].inputs[3]
    )
    # repeat_input_003.edge_index1 -> sample_index_006.Index
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Repeat Input.003"].outputs[2],
        geometry_nodes_1.nodes["Sample Index.006"].inputs[2]
    )
    # edge_vertices_006.Vertex Index 1 -> compare_010.A
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Edge Vertices.006"].outputs[0],
        geometry_nodes_1.nodes["Compare.010"].inputs[2]
    )
    # edge_vertices_006.Vertex Index 2 -> compare_011.A
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Edge Vertices.006"].outputs[1],
        geometry_nodes_1.nodes["Compare.011"].inputs[2]
    )
    # corners_of_edge_003.Corner Index -> sample_index_007.Value
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Corners of Edge.003"].outputs[0],
        geometry_nodes_1.nodes["Sample Index.007"].inputs[1]
    )
    # sample_index_007.Value -> offset_corner_in_face_006.Corner Index
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Sample Index.007"].outputs[0],
        geometry_nodes_1.nodes["Offset Corner in Face.006"].inputs[0]
    )
    # sample_index_007.Value -> offset_corner_in_face_007.Corner Index
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Sample Index.007"].outputs[0],
        geometry_nodes_1.nodes["Offset Corner in Face.007"].inputs[0]
    )
    # offset_corner_in_face_007.Corner Index -> vertex_of_corner_007.Corner Index
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Offset Corner in Face.007"].outputs[0],
        geometry_nodes_1.nodes["Vertex of Corner.007"].inputs[0]
    )
    # offset_corner_in_face_006.Corner Index -> vertex_of_corner_008.Corner Index
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Offset Corner in Face.006"].outputs[0],
        geometry_nodes_1.nodes["Vertex of Corner.008"].inputs[0]
    )
    # vertex_of_corner_007.Vertex Index -> compare_015.B
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Vertex of Corner.007"].outputs[0],
        geometry_nodes_1.nodes["Compare.015"].inputs[3]
    )
    # compare_015.Result -> boolean_math_009.Boolean
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Compare.015"].outputs[0],
        geometry_nodes_1.nodes["Boolean Math.009"].inputs[0]
    )
    # vertex_of_corner_008.Vertex Index -> compare_016.B
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Vertex of Corner.008"].outputs[0],
        geometry_nodes_1.nodes["Compare.016"].inputs[3]
    )
    # compare_016.Result -> boolean_math_009.Boolean
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Compare.016"].outputs[0],
        geometry_nodes_1.nodes["Boolean Math.009"].inputs[1]
    )
    # compare_017.Result -> boolean_math_010.Boolean
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Compare.017"].outputs[0],
        geometry_nodes_1.nodes["Boolean Math.010"].inputs[0]
    )
    # compare_018.Result -> boolean_math_010.Boolean
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Compare.018"].outputs[0],
        geometry_nodes_1.nodes["Boolean Math.010"].inputs[1]
    )
    # vertex_of_corner_007.Vertex Index -> compare_017.B
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Vertex of Corner.007"].outputs[0],
        geometry_nodes_1.nodes["Compare.017"].inputs[3]
    )
    # vertex_of_corner_008.Vertex Index -> compare_018.B
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Vertex of Corner.008"].outputs[0],
        geometry_nodes_1.nodes["Compare.018"].inputs[3]
    )
    # edge_vertices_007.Vertex Index 2 -> compare_017.A
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Edge Vertices.007"].outputs[1],
        geometry_nodes_1.nodes["Compare.017"].inputs[2]
    )
    # edge_vertices_007.Vertex Index 1 -> compare_018.A
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Edge Vertices.007"].outputs[0],
        geometry_nodes_1.nodes["Compare.018"].inputs[2]
    )
    # boolean_math_010.Boolean -> boolean_math_011.Boolean
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Boolean Math.010"].outputs[0],
        geometry_nodes_1.nodes["Boolean Math.011"].inputs[0]
    )
    # boolean_math_009.Boolean -> boolean_math_011.Boolean
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Boolean Math.009"].outputs[0],
        geometry_nodes_1.nodes["Boolean Math.011"].inputs[1]
    )
    # edge_vertices_007.Vertex Index 1 -> compare_015.A
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Edge Vertices.007"].outputs[0],
        geometry_nodes_1.nodes["Compare.015"].inputs[2]
    )
    # edge_vertices_007.Vertex Index 2 -> compare_016.A
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Edge Vertices.007"].outputs[1],
        geometry_nodes_1.nodes["Compare.016"].inputs[2]
    )
    # repeat_input_003.Geometry -> sample_index_007.Geometry
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Repeat Input.003"].outputs[1],
        geometry_nodes_1.nodes["Sample Index.007"].inputs[0]
    )
    # repeat_input_003.edge_index1 -> sample_index_007.Index
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Repeat Input.003"].outputs[2],
        geometry_nodes_1.nodes["Sample Index.007"].inputs[2]
    )
    # boolean_math_008.Boolean -> boolean_math.Boolean
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Boolean Math.008"].outputs[0],
        geometry_nodes_1.nodes["Boolean Math"].inputs[0]
    )
    # boolean_math_011.Boolean -> boolean_math.Boolean
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Boolean Math.011"].outputs[0],
        geometry_nodes_1.nodes["Boolean Math"].inputs[1]
    )
    # index_003.Index -> attribute_statistic_001.Attribute
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Index.003"].outputs[0],
        geometry_nodes_1.nodes["Attribute Statistic.001"].inputs[2]
    )
    # corners_of_edge_004.Corner Index -> sample_index_008.Value
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Corners of Edge.004"].outputs[0],
        geometry_nodes_1.nodes["Sample Index.008"].inputs[1]
    )
    # sample_index_008.Value -> offset_corner_in_face_008.Corner Index
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Sample Index.008"].outputs[0],
        geometry_nodes_1.nodes["Offset Corner in Face.008"].inputs[0]
    )
    # sample_index_008.Value -> offset_corner_in_face_009.Corner Index
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Sample Index.008"].outputs[0],
        geometry_nodes_1.nodes["Offset Corner in Face.009"].inputs[0]
    )
    # offset_corner_in_face_009.Corner Index -> vertex_of_corner_009.Corner Index
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Offset Corner in Face.009"].outputs[0],
        geometry_nodes_1.nodes["Vertex of Corner.009"].inputs[0]
    )
    # offset_corner_in_face_008.Corner Index -> vertex_of_corner_010.Corner Index
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Offset Corner in Face.008"].outputs[0],
        geometry_nodes_1.nodes["Vertex of Corner.010"].inputs[0]
    )
    # vertex_of_corner_009.Vertex Index -> compare_014.B
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Vertex of Corner.009"].outputs[0],
        geometry_nodes_1.nodes["Compare.014"].inputs[3]
    )
    # compare_014.Result -> boolean_math_012.Boolean
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Compare.014"].outputs[0],
        geometry_nodes_1.nodes["Boolean Math.012"].inputs[0]
    )
    # vertex_of_corner_010.Vertex Index -> compare_019.B
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Vertex of Corner.010"].outputs[0],
        geometry_nodes_1.nodes["Compare.019"].inputs[3]
    )
    # compare_019.Result -> boolean_math_012.Boolean
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Compare.019"].outputs[0],
        geometry_nodes_1.nodes["Boolean Math.012"].inputs[1]
    )
    # compare_020.Result -> boolean_math_013.Boolean
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Compare.020"].outputs[0],
        geometry_nodes_1.nodes["Boolean Math.013"].inputs[0]
    )
    # compare_021.Result -> boolean_math_013.Boolean
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Compare.021"].outputs[0],
        geometry_nodes_1.nodes["Boolean Math.013"].inputs[1]
    )
    # vertex_of_corner_009.Vertex Index -> compare_020.B
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Vertex of Corner.009"].outputs[0],
        geometry_nodes_1.nodes["Compare.020"].inputs[3]
    )
    # vertex_of_corner_010.Vertex Index -> compare_021.B
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Vertex of Corner.010"].outputs[0],
        geometry_nodes_1.nodes["Compare.021"].inputs[3]
    )
    # edge_vertices_008.Vertex Index 2 -> compare_020.A
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Edge Vertices.008"].outputs[1],
        geometry_nodes_1.nodes["Compare.020"].inputs[2]
    )
    # edge_vertices_008.Vertex Index 1 -> compare_021.A
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Edge Vertices.008"].outputs[0],
        geometry_nodes_1.nodes["Compare.021"].inputs[2]
    )
    # boolean_math_013.Boolean -> boolean_math_014.Boolean
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Boolean Math.013"].outputs[0],
        geometry_nodes_1.nodes["Boolean Math.014"].inputs[0]
    )
    # boolean_math_012.Boolean -> boolean_math_014.Boolean
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Boolean Math.012"].outputs[0],
        geometry_nodes_1.nodes["Boolean Math.014"].inputs[1]
    )
    # edge_vertices_008.Vertex Index 1 -> compare_014.A
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Edge Vertices.008"].outputs[0],
        geometry_nodes_1.nodes["Compare.014"].inputs[2]
    )
    # edge_vertices_008.Vertex Index 2 -> compare_019.A
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Edge Vertices.008"].outputs[1],
        geometry_nodes_1.nodes["Compare.019"].inputs[2]
    )
    # corners_of_edge_005.Corner Index -> sample_index_009.Value
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Corners of Edge.005"].outputs[0],
        geometry_nodes_1.nodes["Sample Index.009"].inputs[1]
    )
    # sample_index_009.Value -> offset_corner_in_face_010.Corner Index
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Sample Index.009"].outputs[0],
        geometry_nodes_1.nodes["Offset Corner in Face.010"].inputs[0]
    )
    # sample_index_009.Value -> offset_corner_in_face_011.Corner Index
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Sample Index.009"].outputs[0],
        geometry_nodes_1.nodes["Offset Corner in Face.011"].inputs[0]
    )
    # offset_corner_in_face_011.Corner Index -> vertex_of_corner_011.Corner Index
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Offset Corner in Face.011"].outputs[0],
        geometry_nodes_1.nodes["Vertex of Corner.011"].inputs[0]
    )
    # offset_corner_in_face_010.Corner Index -> vertex_of_corner_012.Corner Index
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Offset Corner in Face.010"].outputs[0],
        geometry_nodes_1.nodes["Vertex of Corner.012"].inputs[0]
    )
    # vertex_of_corner_011.Vertex Index -> compare_022.B
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Vertex of Corner.011"].outputs[0],
        geometry_nodes_1.nodes["Compare.022"].inputs[3]
    )
    # compare_022.Result -> boolean_math_015.Boolean
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Compare.022"].outputs[0],
        geometry_nodes_1.nodes["Boolean Math.015"].inputs[0]
    )
    # vertex_of_corner_012.Vertex Index -> compare_023.B
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Vertex of Corner.012"].outputs[0],
        geometry_nodes_1.nodes["Compare.023"].inputs[3]
    )
    # compare_023.Result -> boolean_math_015.Boolean
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Compare.023"].outputs[0],
        geometry_nodes_1.nodes["Boolean Math.015"].inputs[1]
    )
    # compare_024.Result -> boolean_math_016.Boolean
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Compare.024"].outputs[0],
        geometry_nodes_1.nodes["Boolean Math.016"].inputs[0]
    )
    # compare_025.Result -> boolean_math_016.Boolean
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Compare.025"].outputs[0],
        geometry_nodes_1.nodes["Boolean Math.016"].inputs[1]
    )
    # vertex_of_corner_011.Vertex Index -> compare_024.B
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Vertex of Corner.011"].outputs[0],
        geometry_nodes_1.nodes["Compare.024"].inputs[3]
    )
    # vertex_of_corner_012.Vertex Index -> compare_025.B
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Vertex of Corner.012"].outputs[0],
        geometry_nodes_1.nodes["Compare.025"].inputs[3]
    )
    # edge_vertices_009.Vertex Index 2 -> compare_024.A
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Edge Vertices.009"].outputs[1],
        geometry_nodes_1.nodes["Compare.024"].inputs[2]
    )
    # edge_vertices_009.Vertex Index 1 -> compare_025.A
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Edge Vertices.009"].outputs[0],
        geometry_nodes_1.nodes["Compare.025"].inputs[2]
    )
    # boolean_math_016.Boolean -> boolean_math_017.Boolean
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Boolean Math.016"].outputs[0],
        geometry_nodes_1.nodes["Boolean Math.017"].inputs[0]
    )
    # boolean_math_015.Boolean -> boolean_math_017.Boolean
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Boolean Math.015"].outputs[0],
        geometry_nodes_1.nodes["Boolean Math.017"].inputs[1]
    )
    # edge_vertices_009.Vertex Index 1 -> compare_022.A
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Edge Vertices.009"].outputs[0],
        geometry_nodes_1.nodes["Compare.022"].inputs[2]
    )
    # edge_vertices_009.Vertex Index 2 -> compare_023.A
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Edge Vertices.009"].outputs[1],
        geometry_nodes_1.nodes["Compare.023"].inputs[2]
    )
    # boolean_math_014.Boolean -> boolean_math_001.Boolean
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Boolean Math.014"].outputs[0],
        geometry_nodes_1.nodes["Boolean Math.001"].inputs[0]
    )
    # boolean_math_017.Boolean -> boolean_math_001.Boolean
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Boolean Math.017"].outputs[0],
        geometry_nodes_1.nodes["Boolean Math.001"].inputs[1]
    )
    # repeat_input_003.Geometry -> sample_index_008.Geometry
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Repeat Input.003"].outputs[1],
        geometry_nodes_1.nodes["Sample Index.008"].inputs[0]
    )
    # repeat_input_003.Geometry -> sample_index_009.Geometry
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Repeat Input.003"].outputs[1],
        geometry_nodes_1.nodes["Sample Index.009"].inputs[0]
    )
    # repeat_input_003.edge_index2 -> sample_index_008.Index
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Repeat Input.003"].outputs[3],
        geometry_nodes_1.nodes["Sample Index.008"].inputs[2]
    )
    # repeat_input_003.edge_index2 -> sample_index_009.Index
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Repeat Input.003"].outputs[3],
        geometry_nodes_1.nodes["Sample Index.009"].inputs[2]
    )
    # boolean_math.Boolean -> boolean_math_002.Boolean
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Boolean Math"].outputs[0],
        geometry_nodes_1.nodes["Boolean Math.002"].inputs[0]
    )
    # boolean_math_001.Boolean -> boolean_math_002.Boolean
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Boolean Math.001"].outputs[0],
        geometry_nodes_1.nodes["Boolean Math.002"].inputs[1]
    )
    # boolean_math_002.Boolean -> duplicate_elements_001.Selection
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Boolean Math.002"].outputs[0],
        geometry_nodes_1.nodes["Duplicate Elements.001"].inputs[1]
    )
    # group_input.Geometry -> store_named_attribute.Geometry
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Group Input"].outputs[0],
        geometry_nodes_1.nodes["Store Named Attribute"].inputs[0]
    )
    # index.Index -> compare.A
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Index"].outputs[0],
        geometry_nodes_1.nodes["Compare"].inputs[2]
    )
    # integer.Integer -> compare.B
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Integer"].outputs[0],
        geometry_nodes_1.nodes["Compare"].inputs[3]
    )
    # compare.Result -> store_named_attribute.Selection
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Compare"].outputs[0],
        geometry_nodes_1.nodes["Store Named Attribute"].inputs[1]
    )
    # named_attribute_001.Attribute -> mesh_to_curve.Selection
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Named Attribute.001"].outputs[0],
        geometry_nodes_1.nodes["Mesh to Curve"].inputs[1]
    )
    # boolean_math_018.Boolean -> attribute_statistic_001.Selection
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Boolean Math.018"].outputs[0],
        geometry_nodes_1.nodes["Attribute Statistic.001"].inputs[1]
    )
    # boolean_math_002.Boolean -> boolean_math_018.Boolean
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Boolean Math.002"].outputs[0],
        geometry_nodes_1.nodes["Boolean Math.018"].inputs[1]
    )
    # named_attribute_002.Attribute -> boolean_math_019.Boolean
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Named Attribute.002"].outputs[0],
        geometry_nodes_1.nodes["Boolean Math.019"].inputs[0]
    )
    # boolean_math_019.Boolean -> boolean_math_018.Boolean
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Boolean Math.019"].outputs[0],
        geometry_nodes_1.nodes["Boolean Math.018"].inputs[0]
    )
    # repeat_input_003.Geometry -> store_named_attribute_001.Geometry
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Repeat Input.003"].outputs[1],
        geometry_nodes_1.nodes["Store Named Attribute.001"].inputs[0]
    )
    # index_003.Index -> compare_001.B
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Index.003"].outputs[0],
        geometry_nodes_1.nodes["Compare.001"].inputs[3]
    )
    # attribute_statistic_001.Max -> compare_001.A
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Attribute Statistic.001"].outputs[4],
        geometry_nodes_1.nodes["Compare.001"].inputs[2]
    )
    # index_003.Index -> compare_002.B
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Index.003"].outputs[0],
        geometry_nodes_1.nodes["Compare.002"].inputs[3]
    )
    # attribute_statistic_001.Min -> compare_002.A
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Attribute Statistic.001"].outputs[3],
        geometry_nodes_1.nodes["Compare.002"].inputs[2]
    )
    # compare_001.Result -> boolean_math_020.Boolean
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Compare.001"].outputs[0],
        geometry_nodes_1.nodes["Boolean Math.020"].inputs[0]
    )
    # compare_002.Result -> boolean_math_020.Boolean
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Compare.002"].outputs[0],
        geometry_nodes_1.nodes["Boolean Math.020"].inputs[1]
    )
    # boolean_math_020.Boolean -> store_named_attribute_001.Selection
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Boolean Math.020"].outputs[0],
        geometry_nodes_1.nodes["Store Named Attribute.001"].inputs[1]
    )
    # sample_index_010.Value -> index_switch_001.Index
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Sample Index.010"].outputs[0],
        geometry_nodes_1.nodes["Index Switch.001"].inputs[0]
    )
    # boolean_math_022.Boolean -> sample_index_010.Value
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Boolean Math.022"].outputs[0],
        geometry_nodes_1.nodes["Sample Index.010"].inputs[1]
    )
    # repeat_input_003.Geometry -> sample_index_010.Geometry
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Repeat Input.003"].outputs[1],
        geometry_nodes_1.nodes["Sample Index.010"].inputs[0]
    )
    # sample_index_011.Value -> index_switch_002.Index
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Sample Index.011"].outputs[0],
        geometry_nodes_1.nodes["Index Switch.002"].inputs[0]
    )
    # boolean_math_021.Boolean -> sample_index_011.Value
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Boolean Math.021"].outputs[0],
        geometry_nodes_1.nodes["Sample Index.011"].inputs[1]
    )
    # attribute_statistic_001.Min -> sample_index_011.Index
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Attribute Statistic.001"].outputs[3],
        geometry_nodes_1.nodes["Sample Index.011"].inputs[2]
    )
    # attribute_statistic_001.Max -> sample_index_010.Index
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Attribute Statistic.001"].outputs[4],
        geometry_nodes_1.nodes["Sample Index.010"].inputs[2]
    )
    # is_edge_boundary_002.Is Edge Boundary -> boolean_math_021.Boolean
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Is Edge Boundary.002"].outputs[0],
        geometry_nodes_1.nodes["Boolean Math.021"].inputs[0]
    )
    # attribute_statistic_001.Min -> index_switch_002.1
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Attribute Statistic.001"].outputs[3],
        geometry_nodes_1.nodes["Index Switch.002"].inputs[2]
    )
    # index_switch_002.Output -> repeat_output_003.edge_index1
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Index Switch.002"].outputs[0],
        geometry_nodes_1.nodes["Repeat Output.003"].inputs[1]
    )
    # is_edge_boundary_001.Is Edge Boundary -> boolean_math_022.Boolean
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Is Edge Boundary.001"].outputs[0],
        geometry_nodes_1.nodes["Boolean Math.022"].inputs[0]
    )
    # attribute_statistic_001.Max -> index_switch_001.1
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Attribute Statistic.001"].outputs[4],
        geometry_nodes_1.nodes["Index Switch.001"].inputs[2]
    )
    # index_switch_001.Output -> repeat_output_003.edge_index2
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Index Switch.001"].outputs[0],
        geometry_nodes_1.nodes["Repeat Output.003"].inputs[2]
    )
    # attribute_statistic_001.Max -> index_switch_002.0
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Attribute Statistic.001"].outputs[4],
        geometry_nodes_1.nodes["Index Switch.002"].inputs[1]
    )
    # attribute_statistic_001.Min -> index_switch_001.0
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Attribute Statistic.001"].outputs[3],
        geometry_nodes_1.nodes["Index Switch.001"].inputs[1]
    )
    # repeat_input_003.Geometry -> sample_index_011.Geometry
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Repeat Input.003"].outputs[1],
        geometry_nodes_1.nodes["Sample Index.011"].inputs[0]
    )
    # store_named_attribute.Geometry -> repeat_input_004.Geometry
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Store Named Attribute"].outputs[0],
        geometry_nodes_1.nodes["Repeat Input.004"].inputs[1]
    )
    # repeat_output_004.Geometry -> mesh_to_curve.Mesh
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Repeat Output.004"].outputs[0],
        geometry_nodes_1.nodes["Mesh to Curve"].inputs[0]
    )
    # repeat_input_004.Iteration -> repeat_input_003.Iteration
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Repeat Input.004"].outputs[0],
        geometry_nodes_1.nodes["Repeat Input.003"].inputs[5]
    )
    # integer.Integer -> repeat_input_004.Integer
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Integer"].outputs[0],
        geometry_nodes_1.nodes["Repeat Input.004"].inputs[2]
    )
    # integer.Integer -> repeat_input_004.Integer.001
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Integer"].outputs[0],
        geometry_nodes_1.nodes["Repeat Input.004"].inputs[3]
    )
    # repeat_input_004.Integer -> repeat_input_003.edge_index1
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Repeat Input.004"].outputs[2],
        geometry_nodes_1.nodes["Repeat Input.003"].inputs[2]
    )
    # repeat_input_004.Integer.001 -> repeat_input_003.edge_index2
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Repeat Input.004"].outputs[3],
        geometry_nodes_1.nodes["Repeat Input.003"].inputs[3]
    )
    # repeat_input_004.Geometry.001 -> repeat_input_003.Geometry.001
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Repeat Input.004"].outputs[4],
        geometry_nodes_1.nodes["Repeat Input.003"].inputs[4]
    )
    # repeat_output_003.Geometry -> repeat_output_004.Geometry
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Repeat Output.003"].outputs[0],
        geometry_nodes_1.nodes["Repeat Output.004"].inputs[0]
    )
    # repeat_output_003.edge_index1 -> repeat_output_004.Integer
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Repeat Output.003"].outputs[1],
        geometry_nodes_1.nodes["Repeat Output.004"].inputs[1]
    )
    # repeat_output_003.edge_index2 -> repeat_output_004.Integer.001
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Repeat Output.003"].outputs[2],
        geometry_nodes_1.nodes["Repeat Output.004"].inputs[2]
    )
    # repeat_input_004.Geometry -> repeat_input_003.Geometry
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Repeat Input.004"].outputs[1],
        geometry_nodes_1.nodes["Repeat Input.003"].inputs[1]
    )
    # is_edge_boundary_003.Is Edge Boundary -> boolean_math_023.Boolean
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Is Edge Boundary.003"].outputs[0],
        geometry_nodes_1.nodes["Boolean Math.023"].inputs[0]
    )
    # named_attribute_003.Attribute -> boolean_math_023.Boolean
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Named Attribute.003"].outputs[0],
        geometry_nodes_1.nodes["Boolean Math.023"].inputs[1]
    )
    # repeat_input_004.Geometry -> sample_index_012.Geometry
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Repeat Input.004"].outputs[1],
        geometry_nodes_1.nodes["Sample Index.012"].inputs[0]
    )
    # repeat_input_004.Integer -> sample_index_012.Index
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Repeat Input.004"].outputs[2],
        geometry_nodes_1.nodes["Sample Index.012"].inputs[2]
    )
    # boolean_math_023.Boolean -> sample_index_012.Value
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Boolean Math.023"].outputs[0],
        geometry_nodes_1.nodes["Sample Index.012"].inputs[1]
    )
    # repeat_input_004.Integer.001 -> sample_index_013.Index
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Repeat Input.004"].outputs[3],
        geometry_nodes_1.nodes["Sample Index.013"].inputs[2]
    )
    # boolean_math_023.Boolean -> sample_index_013.Value
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Boolean Math.023"].outputs[0],
        geometry_nodes_1.nodes["Sample Index.013"].inputs[1]
    )
    # repeat_input_004.Geometry -> sample_index_013.Geometry
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Repeat Input.004"].outputs[1],
        geometry_nodes_1.nodes["Sample Index.013"].inputs[0]
    )
    # sample_index_012.Value -> boolean_math_024.Boolean
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Sample Index.012"].outputs[0],
        geometry_nodes_1.nodes["Boolean Math.024"].inputs[0]
    )
    # sample_index_013.Value -> boolean_math_024.Boolean
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Sample Index.013"].outputs[0],
        geometry_nodes_1.nodes["Boolean Math.024"].inputs[1]
    )
    # boolean_math_024.Boolean -> index_switch_003.Index
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Boolean Math.024"].outputs[0],
        geometry_nodes_1.nodes["Index Switch.003"].inputs[0]
    )
    # index_switch_003.Output -> repeat_input_003.Iterations
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Index Switch.003"].outputs[0],
        geometry_nodes_1.nodes["Repeat Input.003"].inputs[0]
    )
    # group_input.Geometry -> sample_index_014.Geometry
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Group Input"].outputs[0],
        geometry_nodes_1.nodes["Sample Index.014"].inputs[0]
    )
    # is_edge_boundary_004.Is Edge Boundary -> sample_index_014.Value
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Is Edge Boundary.004"].outputs[0],
        geometry_nodes_1.nodes["Sample Index.014"].inputs[1]
    )
    # integer.Integer -> sample_index_014.Index
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Integer"].outputs[0],
        geometry_nodes_1.nodes["Sample Index.014"].inputs[2]
    )
    # sample_index_014.Value -> switch.Switch
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Sample Index.014"].outputs[0],
        geometry_nodes_1.nodes["Switch"].inputs[0]
    )
    # string_001.String -> switch.True
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["String.001"].outputs[0],
        geometry_nodes_1.nodes["Switch"].inputs[2]
    )
    # string.String -> switch.False
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["String"].outputs[0],
        geometry_nodes_1.nodes["Switch"].inputs[1]
    )
    # switch.Output -> store_named_attribute.Name
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Switch"].outputs[0],
        geometry_nodes_1.nodes["Store Named Attribute"].inputs[2]
    )
    # store_named_attribute_003.Geometry -> join_geometry.Geometry
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Store Named Attribute.003"].outputs[0],
        geometry_nodes_1.nodes["Join Geometry"].inputs[0]
    )
    # group_input.Geometry -> domain_size_001.Geometry
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Group Input"].outputs[0],
        geometry_nodes_1.nodes["Domain Size.001"].inputs[0]
    )
    # domain_size_001.Face Count -> repeat_input_004.Iterations
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Domain Size.001"].outputs[2],
        geometry_nodes_1.nodes["Repeat Input.004"].inputs[0]
    )
    # set_material_001.Geometry -> store_named_attribute_002.Geometry
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Set Material.001"].outputs[0],
        geometry_nodes_1.nodes["Store Named Attribute.002"].inputs[0]
    )
    # set_material.Geometry -> store_named_attribute_003.Geometry
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Set Material"].outputs[0],
        geometry_nodes_1.nodes["Store Named Attribute.003"].inputs[0]
    )
    # set_position.Geometry -> set_material_001.Geometry
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Set Position"].outputs[0],
        geometry_nodes_1.nodes["Set Material.001"].inputs[0]
    )
    # uv_sphere.Mesh -> set_position.Geometry
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["UV Sphere"].outputs[0],
        geometry_nodes_1.nodes["Set Position"].inputs[0]
    )
    # sample_index_003.Value -> set_position.Offset
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Sample Index.003"].outputs[0],
        geometry_nodes_1.nodes["Set Position"].inputs[3]
    )
    # join_geometry.Geometry -> group_output.Geometry
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Join Geometry"].outputs[0],
        geometry_nodes_1.nodes["Group Output"].inputs[0]
    )
    # repeat_output_004.Geometry -> store_named_attribute_004.Geometry
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Repeat Output.004"].outputs[0],
        geometry_nodes_1.nodes["Store Named Attribute.004"].inputs[0]
    )
    # repeat_input_003.Geometry.001 -> join_geometry_003.Geometry
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Repeat Input.003"].outputs[4],
        geometry_nodes_1.nodes["Join Geometry.003"].inputs[0]
    )
    # store_named_attribute_002.Geometry -> join_geometry.Geometry
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Store Named Attribute.002"].outputs[0],
        geometry_nodes_1.nodes["Join Geometry"].inputs[0]
    )
    # store_named_attribute_004.Geometry -> join_geometry.Geometry
    geometry_nodes_1.links.new(
        geometry_nodes_1.nodes["Store Named Attribute.004"].outputs[0],
        geometry_nodes_1.nodes["Join Geometry"].inputs[0]
    )

    return geometry_nodes_1


if __name__ == "__main__":
    # Maps node tree creation functions to the node tree 
    # name, such that we don't recreate node trees unnecessarily
    node_tree_names : dict[typing.Callable, str] = {}

    geometry_nodes = geometry_nodes_1_node_group(node_tree_names)
    node_tree_names[geometry_nodes_1_node_group] = geometry_nodes.name

