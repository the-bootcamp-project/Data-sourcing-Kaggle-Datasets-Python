<a href="https://bootcamp-project.com/" target="_blank"><img src="https://bootcamp-project.com/images/logo.png" align="right" height="200" /></a>

<h1 align="center">Sourcing Kaggle Datasets with Python</h1>

<div align="center">
<img src="https://img.shields.io/badge/security-bandit-yellow.svg?style=for-the-badge"></img>
<img src="https://img.shields.io/pypi/v/sourcing-kaggle-datasets?style=for-the-badge"></img>
<img src="https://img.shields.io/pypi/status/sourcing-kaggle-datasets?style=for-the-badge"></img>
<img src="https://img.shields.io/pypi/implementation/sourcing-kaggle-datasets?style=for-the-badge"></img>
<img src="https://img.shields.io/pypi/pyversions/sourcing-kaggle-datasets?style=for-the-badge"></img>
<img src="https://img.shields.io/pypi/wheel/sourcing-kaggle-datasets?style=for-the-badge"></img>
<img src="https://img.shields.io/pypi/l/sourcing-kaggle-datasets?style=for-the-badge"></img>
<img src="https://img.shields.io/badge/Bootcamp-Project-blue?style=for-the-badge"></img>
</div>

## 👉 About 👈

**Minimum Viable Product**:

### 😎 Built With 😎

- [pytest-dev/pytest](https://github.com/pytest-dev/pytest/)
- [PyCQA/pylint](https://github.com/PyCQA/pylint)
- [PyCQA/bandit](https://github.com/PyCQA/bandit)

## 📖 Getting Started 📖

### ✋ Prerequisites ✋

**Change the project-specific attributes.** See [TODO](TODO.md) for more information.

### 💪 Installation 💪

```bash
pip install --user sourcing-kaggle-datasets
```

## 🚀 Usage 🚀

### 🤓 Static Analysis 🤓

```bash
$ make types
```

```bash
$ make lint
```

```bash
$ make sast
```

```yml
# .gitlab.ci.yml

types:
    stage: Static Analysis
    script: [make types]
    allow_failure: true

linting:
    stage: Static Analysis
    script: [make lint]
    allow_failure: true

secure-code:
    stage: Static Analysis
    script: [make sast]
    allow_failure: false
```

### 🧐 Unit Testing 🧐

```bash
$ make unittests
```

```yml
# .gitlab.ci.yml

unittests:
    stage: Unit Testing
    script: [make unittests]
    allow_failure: false
```

### 🤩 Building 🤩

```bash
$ make build
```

```yml
# .gitlab.ci.yml

build:
    stage: Building
    script: [make build]
    artifacts:
        paths: [dist]
    only:
        - develop
        - main
```

### 🥳 Deployment 🥳

```bash
$ make deploy
```

```yml
# .gitlab.ci.yml

gitlab:
    stage: Deployment
    script: [make deploy]
    artifacts:
        paths: [dist]
    only:
        - develop
        - main

pypi:
    stage: Deployment
    script: [make release]
    artifacts:
        paths: [dist]
    only:
        - main
```

_For more examples, please refer to the [Documentation](https://sourcing-kaggle-datasets-python.rtfm.page)_

## ⭐️ Features ⭐️

- [x] Using **pyTest** as a paradigm for test-driven development
- [x] Using **Bandit** as static application security testing code analyzer
- [x] Automatic build and deploy on **GitLab** and **PyPi** Packages Regestries

## 📑 Changelog 📑

See [CHANGELOG](CHANGELOG) for more information.

## 📋 Roadmap 📋

- [ ] Implement Toml Config Parser as a Settings Mechanism

See the [open issues](https://gitlab.com/the-bootcamp-project/packages/data-science/sourcing-kaggle-datasets-python/-/issues) for a list of proposed features (and known issues).

## 🤝 Contribute 🤝

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Please read the [contribution guidelines](docs/_media/code_of_conduct.md) first.
2. Fork the Project
3. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
4. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
5. Push to the Branch (`git push origin feature/AmazingFeature`)
6. Open a Pull Request

## 📜 License 📜

Distributed under the MIT License. See [LICENSE](LICENSE) for more information.

## 💌 Contact 💌

[Bootcamp contributors](https://bootcamp-project.com/) - `contributors` @ `bootcamp-project` .com

## 🏆 Acknowledgements 🏆

Thanks for these awesome resources that were used during the development of the **Bootcamp Project: Sourcing Kaggle Datasets with Python**:

- [Kaggle API – The Missing Python Documentation](https://technowhisp.com/kaggle-api-python-documentation/)
