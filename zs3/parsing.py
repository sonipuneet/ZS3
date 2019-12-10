import argparse


def get_parser():
    parser = argparse.ArgumentParser(description="PyTorch DeeplabV3Plus Training")
    parser.add_argument(
        "--workers", type=int, default=6, metavar="N", help="dataloader threads"
    )
    parser.add_argument(
        "--freeze-bn",
        type=bool,
        default=False,
        help="whether to freeze bn parameters (default: False)",
    )
    parser.add_argument(
        "--exp_path", type=str, default="run", help="set the checkpoint name"
    )
    parser.add_argument(
        "--seed", type=int, default=1, metavar="S", help="random seed (default: 1)"
    )
    parser.add_argument(
        "--no-cuda", action="store_true", default=False, help="disables CUDA training"
    )
    parser.add_argument(
        "--gpu-ids",
        type=str,
        default="0",
        help="use which gpu to train, must be a \
                            comma-separated list of integers only (default=0)",
    )
    return parser
