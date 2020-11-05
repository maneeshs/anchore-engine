# coding: utf-8


from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from anchore_engine.services.policy_engine.api.models.base_model_ import Model
from anchore_engine.services.policy_engine.api import util


class ImageUpdateNotification(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(
        self, image_id=None, user_id=None, analysis_url=None, event_timestamp=None
    ):  # noqa: E501
        """ImageUpdateNotification - a model defined in Swagger

        :param image_id: The image_id of this ImageUpdateNotification.  # noqa: E501
        :type image_id: str
        :param user_id: The user_id of this ImageUpdateNotification.  # noqa: E501
        :type user_id: str
        :param analysis_url: The analysis_url of this ImageUpdateNotification.  # noqa: E501
        :type analysis_url: str
        :param event_timestamp: The event_timestamp of this ImageUpdateNotification.  # noqa: E501
        :type event_timestamp: datetime
        """
        self.swagger_types = {
            "image_id": str,
            "user_id": str,
            "analysis_url": str,
            "event_timestamp": datetime,
        }

        self.attribute_map = {
            "image_id": "image_id",
            "user_id": "user_id",
            "analysis_url": "analysis_url",
            "event_timestamp": "event_timestamp",
        }

        self._image_id = image_id
        self._user_id = user_id
        self._analysis_url = analysis_url
        self._event_timestamp = event_timestamp

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ImageUpdateNotification of this ImageUpdateNotification.  # noqa: E501
        :rtype: ImageUpdateNotification
        """
        return util.deserialize_model(dikt, cls)

    @property
    def image_id(self):
        """Gets the image_id of this ImageUpdateNotification.


        :return: The image_id of this ImageUpdateNotification.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this ImageUpdateNotification.


        :param image_id: The image_id of this ImageUpdateNotification.
        :type image_id: str
        """

        self._image_id = image_id

    @property
    def user_id(self):
        """Gets the user_id of this ImageUpdateNotification.


        :return: The user_id of this ImageUpdateNotification.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this ImageUpdateNotification.


        :param user_id: The user_id of this ImageUpdateNotification.
        :type user_id: str
        """

        self._user_id = user_id

    @property
    def analysis_url(self):
        """Gets the analysis_url of this ImageUpdateNotification.

        A url that can be used to retrieve the analysis information on the image  # noqa: E501

        :return: The analysis_url of this ImageUpdateNotification.
        :rtype: str
        """
        return self._analysis_url

    @analysis_url.setter
    def analysis_url(self, analysis_url):
        """Sets the analysis_url of this ImageUpdateNotification.

        A url that can be used to retrieve the analysis information on the image  # noqa: E501

        :param analysis_url: The analysis_url of this ImageUpdateNotification.
        :type analysis_url: str
        """

        self._analysis_url = analysis_url

    @property
    def event_timestamp(self):
        """Gets the event_timestamp of this ImageUpdateNotification.

        The time of the external event. Should be set to when the event occurred, to the delivery time  # noqa: E501

        :return: The event_timestamp of this ImageUpdateNotification.
        :rtype: datetime
        """
        return self._event_timestamp

    @event_timestamp.setter
    def event_timestamp(self, event_timestamp):
        """Sets the event_timestamp of this ImageUpdateNotification.

        The time of the external event. Should be set to when the event occurred, to the delivery time  # noqa: E501

        :param event_timestamp: The event_timestamp of this ImageUpdateNotification.
        :type event_timestamp: datetime
        """

        self._event_timestamp = event_timestamp
