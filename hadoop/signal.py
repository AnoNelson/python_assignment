from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.dispatch import receiver
import logging

from hadoop import utils

# Get the auth logger
auth_logger = logging.getLogger('django.contrib.auth')


@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    hdfs_profile_pic_path = utils.upload_to_hdfs()
    print("output: ", hdfs_profile_pic_path)
    auth_logger.info(f'login User {user.username} successfully logged in')


@receiver(user_logged_out)
def log_user_logout(sender, request, user, **kwargs):
    hdfs_profile_pic_path = utils.upload_to_hdfs()
    print("output: ", hdfs_profile_pic_path)
    auth_logger.info(f'logout User {user.username} successfully logged out')


@receiver(user_login_failed)
def log_user_login_failed(sender, credentials, request, **kwargs):
    hdfs_profile_pic_path = utils.upload_to_hdfs()
    print("output: ", hdfs_profile_pic_path)
    username = credentials.get('username', 'GUEST')  # Get username from credentials
    auth_logger.warning(f'login User {username} failed to log in')
