from escola.models import Estudante,Curso,Matricula
from escola.serializers import EstudanteSerializer,CursoSerializer,MatriculaSerializer,ListaMatriculasCursoSerializer,ListaMatriculasEstudantesSerializer
from rest_framework import viewsets,generics

class EstudanteViewSet(viewsets.ModelViewSet):
    queryset = Estudante.objects.all()
    serializer_class = EstudanteSerializer

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer

class ListaMatriculaEstudante(generics.ListAPIView):
    
    serializer_class = ListaMatriculasEstudantesSerializer
    def get_queryset(self):
        queryset = Matricula.objects.filter(estudante__id = self.kwargs['pk'])
        return queryset

class ListaMatriculaCurso(generics.ListAPIView):

    serializer_class = ListaMatriculasCursoSerializer
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso__id = self.kwargs['pk'])
        return queryset