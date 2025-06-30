"""
Test commands for the core app.
"""

from unittest.mock import patch
from psycopg2 import OperationalError as Psycopg2OperationalError

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase

class CommandTests(SimpleTestCase):
    """Test commands."""

    @patch('core.management.commands.wait_for_db.Command.check')
    def test_wait_for_db_ready(self, patched_check):
        """Test waiting for db when db is available."""
        patched_check.return_value = True

        call_command('wait_for_db')

        patched_check.assert_called_once_with(databases=['default'])

    @patch('time.sleep')
    @patch('core.management.commands.wait_for_db.Command.check')
    def test_wait_for_db_delay(self, patched_check, patched_sleep):
        """Test waiting for db when getting OperationalError."""
        patched_check.side_effect = [Psycopg2OperationalError] * 2 + [True]

        call_command('wait_for_db')

        self.assertEqual(patched_check.call_count, 3)
        patched_sleep.assert_called_once_with(1)