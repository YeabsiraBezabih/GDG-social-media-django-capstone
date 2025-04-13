from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import Post, Like, Comment, UserProfile, Follow
from .serializers import CommentSerializer, UserProfileSerializer,FollowUnfollowSerializer,LikeToggleSerializer
from django.contrib.auth.models import User


class LikeToggleView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = LikeToggleSerializer
    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        like, created = Like.objects.get_or_create(user=request.user, post=post)

        if not created:
            like.delete()
            return Response({'status': 'unliked'}, status=status.HTTP_200_OK)

        return Response({'status': 'liked'}, status=status.HTTP_201_CREATED)


class CommentListCreateView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        return Comment.objects.filter(post_id=post_id).order_by('-timestamp')

    def perform_create(self, serializer):
        post_id = self.kwargs['post_id']
        serializer.save(user=self.request.user, post_id=post_id)

    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        user_id = self.kwargs['user_id']
        user = get_object_or_404(User, id=user_id)  # Check the User model first
        
        user_profile, created = UserProfile.objects.get_or_create(user=user)
        return user_profile

    def update(self, request, *args, **kwargs):
        user_profile = self.get_object()
        user = user_profile.user

        
        user.username = request.data.get('username', user.username)
        user.save()

       
        user_profile.bio = request.data.get('bio', user_profile.bio)
        user_profile.save()

        return Response({
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "bio": user_profile.bio
        }, status=status.HTTP_200_OK)


class FollowUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = FollowUnfollowSerializer
    def post(self, request, user_id):
        user_to_follow = get_object_or_404(User, id=user_id)
        if request.user == user_to_follow:
            return Response({"message": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        follow, created = Follow.objects.get_or_create(follower=request.user, following=user_to_follow)
        if created:
            return Response({"message": f"You are now following {user_to_follow.username}"}, status=status.HTTP_201_CREATED)
        return Response({"message": f"You are already following {user_to_follow.username}"}, status=status.HTTP_200_OK)


class UnfollowUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = FollowUnfollowSerializer
    def post(self, request, user_id):
        user_to_unfollow = get_object_or_404(User, id=user_id)
        follow = Follow.objects.filter(follower=request.user, following=user_to_unfollow).first()

        if follow:
            follow.delete()
            return Response({"message": f"You have unfollowed {user_to_unfollow.username}"}, status=status.HTTP_200_OK)
        return Response({"message": f"You are not following {user_to_unfollow.username}"}, status=status.HTTP_400_BAD_REQUEST)
