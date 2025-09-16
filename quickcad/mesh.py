import FreeCAD
import Points
import Mesh

# 1. Criar um novo documento
doc = FreeCAD.newDocument("PointCloudToMesh")

# 2. Importar nuvem de pontos (ex.: arquivo .asc, .xyz ou .ply)
# Obs: substitua o caminho abaixo pelo seu arquivo
point_file = "/caminho/para/sua_nuvem.asc"
points = Points.importPoints(point_file)

# Adicionar ao documento como objeto
pc = doc.addObject("Points::Import", "PointCloud")
pc.Source = point_file

# 3. Converter a nuvem em Mesh (triangulação)
#   Exemplo: usar triangulação Delaunay
mesh_obj = Mesh.Mesh()
mesh_obj.addFacet((0,0,0), (1,0,0), (0,1,0))  # exemplo: face manual

# Para reconstruir mesh da nuvem:
import MeshPart
shape = MeshPart.meshFromPoints(points.Points)

# 4. Adicionar ao documento
mesh = doc.addObject("Mesh::Feature", "MeshFromPointCloud")
mesh.Mesh = shape

doc.recompute()
Mesh.export([mesh], "malha.stl")