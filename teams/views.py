from rest_framework.views import APIView, Response, Request, status;
from django.forms.models import model_to_dict;
from .utils import data_processing, NegativeTitlesError, InvalidYearCupError, ImpossibleTitlesError;
from .models import Team;

class TeamView(APIView):

    #Lista todas as seleções

    def get(self, request: Request) -> Response:
        
        teams = Team.objects.all()

        teams_list = []

        for team in teams:
            team_dict = model_to_dict(team)
            teams_list.append(team_dict)

        return Response(teams_list, status=status.HTTP_200_OK)

    def post(self, request: Request) -> Response:

        data = request.data
            
        try:
            data = data_processing(data)
            team = Team.objects.create(**data)
            team_dict = model_to_dict(team)
        except (NegativeTitlesError, InvalidYearCupError, ImpossibleTitlesError) as e:
            return Response({"error": e.args[0]}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(team_dict, status=status.HTTP_201_CREATED)

class TeamParamView(APIView):
    
        def get(self, request: Request, pk: int) -> Response:
    
            try:
                team = Team.objects.get(id=pk)
                team_dict = model_to_dict(team)
            except Team.DoesNotExist:
                return Response({"message": "Team not found"}, status=status.HTTP_404_NOT_FOUND)
            
            return Response(team_dict, status=status.HTTP_200_OK)
    
        def patch(self, request: Request, pk: int) -> Response:
    
            data = request.data
    
            try:
                team = Team.objects.get(id=pk)
                for key, value in data.items():
                    setattr(team, key, value)
                team.save()
                team_dict = model_to_dict(team)
            except Team.DoesNotExist:
                return Response({"message": "Team not found"}, status=status.HTTP_404_NOT_FOUND)
            
            return Response(team_dict, status=status.HTTP_200_OK);
    
        def delete(self, request: Request, pk: int) -> Response:
    
            try:
                team = Team.objects.get(id=pk)
            except Team.DoesNotExist:
                return Response({"message": "Team not found"}, status=status.HTTP_404_NOT_FOUND)
            
            team.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)