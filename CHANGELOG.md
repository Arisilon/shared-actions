# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Add build-documentation action and call from python-cicd. (GitHub #30)

## [7.2.0] - 2026-05-31

### Added

- Add update-changelog to python-cicd workflow. (GitHub #29)

### Changed

- Don't run ci on change log update. (GitHub #29)

## [7.1.1] - 2026-05-30

### Changed

- Fix update-changelog action. (GitHub #28)

### Removed

- Remove setup-python caching from vjer and update-changelog. (GitHub #28)

## [7.1.0] - 2026-05-29

### Added

- Add support for updating a release tag to the latest version.
- Add changelog automation support to the Python CI/CD workflow. (GitHub #26)

### Changed

- Implement change log automation. (GitHub #26)
- Fix release tag parsing.
- Update this change log on release. (GitHub #26)
- Fix fetch-depth on new update-changelog action. (GitHub #26)
- Need fetch-depth=0 for update-changelog. (GitHub #26)
- Install git-cliff from requirements.txt file. (GitHub #26)
- Need to update repo state after release for change log update. (GitHub #26)
- Need to sync branch before git-cliff update. (GitHub #26)

## [7.0.1] - 2026-05-25

### Changed

- Use new release tag in vjer.
- Only download artifacts on release actions. (GitHub #25)
- Use released branch after testing.

## [7.0.0] - 2026-05-22

### Changed

- Update readme.
- Publish test results as they occur. (GitHub #24)
- Rename test-action input to install-test-action.
- Use OS specific actions. (GitHub #24)
- Fix action path. (GitHub #24)
- Update change log.
- Restore removed release steps.

## [6.0.0] - 2026-05-21

### Added

- Added release action. (GitHub #3)
- Add requirements.txt for Python setup. (GitHub #3)
- Add released tag. (GitHub #3)

### Changed

- Changed the default Python usage to 3.14. (GitHub #23)
- Python 3.15 is not yet available for testing.
- Don't set pyproject-build on default.
- Fix the vjer step name. (GitHub #3)
- Final updates for release.

## [5.0.2] - 2026-03-01

### Changed

- Test merge-multiple option.
- Set path for artifacts
- Fix vjer action artifact download when no artifacts. (GitHub #21)

## [5.0.1] - 2026-03-01

### Changed

- Fix vjer action artifact download. (GitHub #20)
- Test fix.
- Revert to released branch after testing.

## [5.0.0] - 2026-02-20

### Changed

- Set fail-fast to false for Python CI/CD tests. (GitHub #19)
- Publish all test results.
- Parameterize the OS and version lists.

## [4.2.2] - 2026-02-12

### Changed

- Update all remote action versions.
- Update change log.
- Fix README formatting.

## [4.2.1] - 2026-02-10

### Added

- Add correct permission.
- Add needed permission.
- Add new missing permission.

### Changed

- Allow test results to be published in PR comments.
- Update change log.

## [4.2.0] - 2026-02-09

### Added

- Add PYthon 3.14 to Python tests. (GitHub #16)

### Changed

- Update change log.

## [4.1.0] - 2025-05-01

### Added

- Added support for VJER_DOCKER_PUSH. (GitHub #15)

## [4.0.1] - 2025-04-27

### Changed

- Set GH_TOKEN on release (GitHub #14)

## [4.0.0] - 2025-04-27

### Added

- Added pass in of GitHub token during checkout. (GitHub #11)
- Add Python CI/CD workflow.
- Add rc_release.
- Add vjer-local Add vjer-version options to new CI/CD workflow.

### Changed

- Fix typo.
- Fix checkout with no token.
- Fix syntax.
- Improve argument handling.
- Fix job name.
- Set permissions at calling workflow.
- Use release environment for rc_release.
- Need separate environment for rc_release.
- Allow skipping the PyPi test.
- Fix variable name.
- Fix Vjer config file name.
- Merge remote-tracking branch 'refs/remotes/origin/main'
- Update change log.
- Replace test PyPi with RC release.
- The rc-release is a pre_release action.
- Fix vjer-version usage.

### Removed

- Remove redundant variables. (GitHub #11)

## [3.0.0] - 2025-04-21

### Added

- Added support for test PyPi on local Vjer install . (GitHub #9)
- Add new option to the command.
- Add cross-platform action.
- Add debugging output.
- Add test action.
- Add redirection.
- Add use-pypi-test input to install test.
- Add environment access.

### Changed

- Fix pip command usage.
- Use standard extension.
- Fix action reference.
- Try a test re-usable workflow.
- Fix re-usable test workflow.
- Fix action call.
- Update action call.
- Change subprocess call.
- Fix pip usage.
- Fix reusable workflow.
- Take more inputs.
- Simplify action.
- Convert vjer from workflow to action.
- Secrets must be passed in.
- Fix syntax.
- Update change log.
- Merge pull request #11 from Arisilon/feature/vjer-action
- Fix pip usage on Windows.
- Download artifacts on releases.
- Update action.yaml
- Update CHANGELOG.md

### Removed

- Remove shell command option.

## [2.2.1] - 2025-04-19

### Changed

- Fixed Vjer install on Windows. (GitHub #8)
- Update README.md
- Fix conditional logic.
- Need quotes around variables.
- Update CHANGELOG.md.

## [2.2.0] - 2025-04-18

### Added

- Added support for enabling git commit during action. (GitHub #6)
- Added support for passing in the build number. (GitHub #7)

### Changed

- Update change log.

## [2.1.0] - 2025-04-12

### Added

- Added support for specifying vjer version. (GitHub #5)
- Added support for specifying PyPi test. (GitHub #5)

### Changed

- Update readme.
- Fix PyPi test install. (GitHub #5)
- Pass Dockerhub credentials.
- Update the change log.

## [2.0.0] - 2025-04-06

### Changed

- Fix var usage.
- VJER_USE_FLIT must be a string.
- Update change log.
- Set build number.
- Update for new Vjer usage.

## [1.0.1] - 2025-02-12

### Added

- Add change log.

### Changed

- Updated remote actions to latest versions. (GitHub #2)

## [1.0.0] - 2025-01-01

### Added

- Add artufact upload for builds.
- Add install-test action.
- Add pypi-publish action.
- Add unit test upload.

### Changed

- Initial commit
- Save test job.
- Fix variable ref.
- Fix action location.
- Fix var usage.
- Create an action for vjer.
- Improve install testing.
- Allow vjer to be run for testing.
- Pass in vjer controlls.
- Set VJER_ENV.
- Improve publishing.
- Need to checkout source to setup Python.
- Pass in the run-id.
- Change variable name.
- Create an action to test variables.
- Update the var test action.
- Change variable type.
- Change run id var type.
- Pass download token.
- Download artifacts before calling shared action.
- Try inherited secrets.
- Use local vjer when available.
- Fix order and name the step.
- Upload unit test results without publish.
- Only download artifacts from build.
- Fix unit test directory name.
- Need to test actions.
- Fix artifact download.
- Update Python action.
- Update publishing shared workflow.

### Removed

- Remove spelling words.
- Remove test code.

[unreleased]: https://github.com/Arisilon/shared-actions/compare/7.2.0..HEAD
[7.2.0]: https://github.com/Arisilon/shared-actions/compare/7.1.1..7.2.0
[7.1.1]: https://github.com/Arisilon/shared-actions/compare/7.1.0..7.1.1
[7.1.0]: https://github.com/Arisilon/shared-actions/compare/7.0.1..7.1.0
[7.0.1]: https://github.com/Arisilon/shared-actions/compare/7.0.0..7.0.1
[7.0.0]: https://github.com/Arisilon/shared-actions/compare/6.0.0..7.0.0
[6.0.0]: https://github.com/Arisilon/shared-actions/compare/v5.0.2..6.0.0
[5.0.2]: https://github.com/Arisilon/shared-actions/compare/v5.0.1..v5.0.2
[5.0.1]: https://github.com/Arisilon/shared-actions/compare/v5.0.0..v5.0.1
[5.0.0]: https://github.com/Arisilon/shared-actions/compare/v4.2.2..v5.0.0
[4.2.2]: https://github.com/Arisilon/shared-actions/compare/v4.2.1..v4.2.2
[4.2.1]: https://github.com/Arisilon/shared-actions/compare/v4.2.0..v4.2.1
[4.2.0]: https://github.com/Arisilon/shared-actions/compare/v4.1.0..v4.2.0
[4.1.0]: https://github.com/Arisilon/shared-actions/compare/v4.0.1..v4.1.0
[4.0.1]: https://github.com/Arisilon/shared-actions/compare/v4.0.0..v4.0.1
[4.0.0]: https://github.com/Arisilon/shared-actions/compare/v3.0.0..v4.0.0
[3.0.0]: https://github.com/Arisilon/shared-actions/compare/v2.2.1..v3.0.0
[2.2.1]: https://github.com/Arisilon/shared-actions/compare/v2.2.0..v2.2.1
[2.2.0]: https://github.com/Arisilon/shared-actions/compare/v2.1.0..v2.2.0
[2.1.0]: https://github.com/Arisilon/shared-actions/compare/v2.0.0..v2.1.0
[2.0.0]: https://github.com/Arisilon/shared-actions/compare/v1.0.1..v2.0.0
[1.0.1]: https://github.com/Arisilon/shared-actions/compare/v1.0.0..v1.0.1
[1.0.0]: https://github.com/Arisilon/shared-actions/tree/v1.0.0

<!-- generated by git-cliff -->
