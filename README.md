# ci-multi-arch-native-test

[![Travis Status](https://travis-ci.com/junaruga/ci-multi-arch-native-test.svg?branch=master)](https://travis-ci.com/junaruga/ci-multi-arch-native-test)
[![GitHub Actions Build](https://github.com/junaruga/ci-multi-arch-native-test/actions/workflows/build.yml/badge.svg)](https://github.com/junaruga/ci-multi-arch-native-test/actions/workflows/build.yml)

CI multiple CPU architectures test.
This repository is focusing to test Travis CI native multiple architectures features [1].
The Travis `arch: arm64`, `arch: ppc64le`, `arch: s390x` have the free unlimited builds without credits for open source software repositories [2][3].

## Sister projects

* [ci-multi-arch-native-container-test](https://github.com/junaruga/ci-multi-arch-native-container-test): This project is focusing native + Fedora container, without QEMU emulation.
* [ci-multi-arch-test](https://github.com/junaruga/ci-multi-arch-test): This project has both some CIs native and QEMU emulated architecture cases.

## References

* [1] https://blog.travis-ci.com/2019-11-12-multi-cpu-architecture-ibm-power-ibm-z
* [2] https://docs.travis-ci.com/user/billing-overview/#partner-queue-solution
* [3] https://bugs.ruby-lang.org/issues/17818#note-3
