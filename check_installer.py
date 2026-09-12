"""Check that replacing a skill preserves both directories and linked source files."""
import importlib.util
from pathlib import Path
import tempfile
from unittest.mock import patch

spec = importlib.util.spec_from_file_location('installer', Path(__file__).with_name('install.py'))
installer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(installer)
with tempfile.TemporaryDirectory() as scratch:
    root = Path(scratch)
    target = root / 'skills/hyperframes'
    target.mkdir(parents=True)
    (target / 'existing.txt').write_text('keep this work')
    with patch.object(Path, 'home', return_value=root):
        installer.install_skill(target)
        assert (target / 'SKILL.md').is_file()
        backups = root / '.local/share/hyperframes/backups'
        assert any(p.read_text() == 'keep this work' for p in backups.glob('*/hyperframes/existing.txt'))
        linked_source = root / 'linked-source'
        linked_source.mkdir()
        (linked_source / 'existing.txt').write_text('linked work')
        link = root / 'linked-skills/hyperframes'
        link.parent.mkdir()
        link.symlink_to(linked_source, target_is_directory=True)
        installer.install_skill(link)
        assert not link.is_symlink() and (link / 'SKILL.md').is_file()
        assert (linked_source / 'existing.txt').read_text() == 'linked work'
        assert any(p.is_symlink() for p in backups.glob('*/hyperframes'))
print('PASS: existing directories and symlink sources remain recoverable.')
